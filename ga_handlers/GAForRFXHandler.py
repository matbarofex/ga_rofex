# -*- coding: utf-8 -*-

from flask import make_response, jsonify
from datetime import datetime
from bisect import bisect_left

import logging
import connector_pmy_api.pmy_rest_api as api
import configuration.config as config
import configuration.ga_responses as responses


class GAForRFXHandler:
    """
    Implementation of the GABaseHandler.
    """

    def __init__(self):
        self.restClient = api.RestClient(config.PrimaryAPI.USER, config.PrimaryAPI.PASS, config.PrimaryAPI.ENVIRONMENT)
        self.restClient.login()

    def process_request(self, request):
        """
        Method to process the input Alexa request and
        dispatch to the appropriate on_ handler
        :param request:
        :return: response from the on_ handler
        """

        logging.info("Process Request: " + str(request))

        try:
            response = None
            # Check the language of the request
            lan = request['queryResult']['languageCode']
            if lan.__contains__("es"):
                lan = config.Language.ES
            elif lan.__contains__("en"):
                lan = config.Language.EN
            else:
                # IF THE LANGUAGE IS NOT SUPPORTED
                response = self.on_language_not_supported(request, lan)

            response = self.on_intent(request, lan)

        except Exception as exc:
            response = self.on_processing_error(request, exc, lan)

        logging.info("Response: " + response)
        return make_response(jsonify({'fulfillmentText': response}))

    def on_intent(self, request, lan):
        """ Process user Intent and return appropriate response"""

        intent = request.get("queryResult").get('intent').get('displayName')

        logging.info('Intent: ' + str(intent))

        if intent == 'Default Welcome Intent':
            return self.on_welcome_intent(request, lan)
        elif intent == 'Last Price Intent':
            return self.on_last_price_intent(request, lan)
        elif intent == 'Help Intent':
            return self.on_help_intent(request, lan)
        elif intent == 'List Intent':
            return self.on_list_intent(request, lan)
        else:
            logging.error('Unexpected Intent.')
            return GAForRFXHandler._default_response(lan)

    def on_processing_error(self, request, exc, lan):
        logging.error("on processing error \n" + str(exc))
        return GAForRFXHandler._error_response(lan)

    def on_welcome_intent(self, launch_request, lan):
        logging.debug("in on_welcome_intent...")
        return GAForRFXHandler._init_response(lan)

    def on_language_not_supported(self, lan):
        logging.debug("in on_language_not_supported...")
        return GAForRFXHandler._language_not_supported_response(lan)

    def on_help_intent(self, request, lan):
        logging.debug("in on_help_intent...")
        return GAForRFXHandler._help_response(lan)

    def on_list_intent(self, request, lan):
        logging.debug("in on_list_intent...")
        return GAForRFXHandler._list_response(lan)

    def _init_response(lan):
        return responses.INIT_RESPONSE[lan]

    def _language_not_supported_response(lan):
        return responses.LANG_NOT_SUPPORTED[lan]

    def _help_response(lan):
        return responses.HELP_RESPONSE[lan]

    def _list_response(lan):
        return responses.LIST_RESPONSE[lan]

    def _default_response(lan):
        return responses.DEFAULT_RESPONSE[lan]

    def _error_response(lan):
        return responses.ERROR_RESPONSE[lan]

    def on_last_price_intent(self, req, lan):

        logging.debug("in on_last_price_intent...")

        # Get request Parameters
        parameters = req['queryResult']['parameters']

        # Check if product parameter exist
        if parameters.get('product'):

            product = parameters.get('product')
            logging.debug("Product + " + str(product))

            if product.__contains__("Spot"):

                api_response = self.restClient.market_data(config.Instrument[product]['initials'], 'IV')

                if api_response['marketData']['IV']:
                    response = responses.LAST_PRICE_OK_RESPONSE_SPOT[lan].format(config.Instrument[product]['name'][lan],
                                                                                 str(api_response['marketData']['IV']))
                else:
                    response = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]
            else:
                if parameters.get('month'):
                    month = parameters.get('month')
                    instrument = self._get_instrument(product, lan, month)
                else:
                    instrument = self._get_instrument(product, lan)

                logging.debug("Instrument: " + str(instrument))

                api_response = self.restClient.market_data(instrument['ticker'], 'LA,SE')

                if api_response['status'] == 'ERROR':
                    response = responses.LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE[lan].format(instrument['prod'],
                                                                                              instrument['month'],
                                                                                              config.Month[
                                                                                                  str(GAForRFXHandler.find_closest_month(product))
                                                                                              ]['text'][lan])
                else:
                    last_price_response = api_response['marketData']['LA']
                    settlement_price_response = api_response['marketData']['SE']
                    if last_price_response:
                        response = responses.LAST_PRICE_OK_RESPONSE[lan].format(
                            instrument['prod'],
                            instrument['month'],
                            str(last_price_response['price']))
                    elif settlement_price_response:
                        response = responses.SETTLE_PRICE_OK_RESPONSE[lan].format(
                            instrument['prod'],
                            instrument['month'],
                            str(settlement_price_response['price']))
                    else:
                        response = responses.LAST_PRICE_MD_NOT_FOUND_RESPONSE[lan]
        else:
            response = responses.LAST_PRICE_ERROR_RESPONSE[lan].format(parameters.get('product'))

        return response

    def _get_instrument(self, product_id, lan, month_id=-1):
        instrument = {"ticker": "", "month":""}
        if product_id in config.Instrument.keys():
            if month_id == -1:
                month_id = str(GAForRFXHandler.find_closest_month(product_id))
            year = str(datetime.now().year)[2:]
            if int(month_id) < datetime.now().month:
                year = str(datetime.now().year + 1)[2:]
            instrument['ticker'] = config.Instrument[product_id]['initials'] + config.Month[month_id]['initials'] + year
            instrument['month'] = config.Month[month_id]['text'][lan]
            instrument['prod'] = config.Instrument[product_id]['name'][lan]
        else:
            logging.warning("Instrument not found for product_ id " + product_id)
        return instrument

    def find_closest_month(product_id):
        close = bisect_left(config.Instrument[product_id]['trade_months'], datetime.now().month)
        if close == len(config.Instrument[product_id]['trade_months']):
            close = 0
        return config.Instrument[product_id]['trade_months'][close]
