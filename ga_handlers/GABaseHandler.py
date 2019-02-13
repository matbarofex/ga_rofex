import abc
import logging
import configuration.config as config
from flask import make_response, jsonify

class GABaseHandler(object):
    """
    Base class for a Alexa Skill Set.  Concrete implementations
    are expected to implement the abstract methods.

    See the following for Alexa details:
    https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/handling-requests-sent-by-alexa
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        logging.basicConfig()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

    @abc.abstractmethod
    def on_launch(self, launch_request, session, lan):
        """
        Implement the LaunchRequest.  Called when the user issues a:
        Alexa, open <invocation name>
        :param launch_request:
        :param session:
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_intent(self, intent_request, session, lan):
        """
        Implement the IntentRequest
        :param intent_request:
        :param session:
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_processing_error(self, event, context, exc, lan):
        """
        If an unexpected error occurs during the process_request method
        this handler will be invoked to give the concrete handler
        an opportunity to respond gracefully

        :param exc exception instance
        :return: the output of _build_response
        """
        pass

    @abc.abstractmethod
    def on_language_not_supported(self, lan):
        """
        If the language of the request is not supported
        this handler will respond appropriately

        :param lan language not supported
        :return: the output of _build_response
        """
        pass

    def process_request(self, request):
        """
        Method to process the input Alexa request and
        dispatch to the appropriate on_ handler
        :param event:
        :param context:
        :return: response from the on_ handler
        """
        self.logger.info(request)
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
                response = self.on_languague_not_supported(request, lan)

            response = self.on_intent(request, lan)

            self.logger.info("RESPONSE:" + response)

        except Exception as exc:
            response = self.on_processing_error(request, exc, lan)

        return make_response(jsonify({'fulfillmentText': response}))

