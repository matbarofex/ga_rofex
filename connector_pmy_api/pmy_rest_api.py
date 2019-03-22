# coding: utf-8

import requests
import simplejson
import logging

from connector_pmy_api.pmy_enums import Entorno
from connector_pmy_api.pmy_exceptions import PMYAPIException


class RestClient:

    # Endpoints
    endpointRestDemo = "http://demo-api.primary.com.ar/"
    endpointRestRemarket = "http://http://pbcp-remarket.cloud.primary.com.ar/"
    endpointRestProd = "https://api.primary.com.ar/"

    def __init__(self, user, password, entorno, account=0):

        self.user = user
        self.password = password
        self.account = account
        self.token = None
        self.islogin = False
        self.initialized = True
        self.marketID = "ROFX"
        self.entorno = entorno

        if self.entorno.value is Entorno.DEMO.value:
            self.activeEndpoint = RestClient.endpointRestDemo
            self.verify_https = False
        elif self.entorno.value is Entorno.PROD.value:
            self.activeEndpoint = RestClient.endpointRestProd
            self.verify_https = True
        elif self.entorno.value is Entorno.REMARKET.value:
            self.activeEndpoint = RestClient.endpointRestRemarket
            self.verify_https = False
        else:
            self.initialized = False
            raise PMYAPIException("Incorrect Environment.")

    def api_request(self, url, login=True):
        try:
            if not self.islogin:
                if self.login():
                    return self.api_request(url, False)
                else:
                    raise PMYAPIException("Could not Authenticate.")
            else:
                headers = {'X-Auth-Token': self.token}

                logging.debug("Request: " + url)
                r = requests.get(url, headers=headers, verify=self.verify_https)
                logging.debug("Response Status: " + str(r.status_code))
                logging.debug("Response Content: " + str(r.content))
                if r.status_code == 401:
                    raise PMYAPIException("Token Invalido.")
                else:
                    return simplejson.loads(r.content)
        except Exception as e:
            raise PMYAPIException("Ocurrió un error con el request.", e)

    def market_data(self, symbol, entries):
        url = self.activeEndpoint + "rest/marketdata/get?marketId={m}&symbol={s}&entries={e}".format(m=self.marketID,s=symbol,e=entries)
        return self.api_request(url)

    def login(self):

        # Validamos que se inicializaron los parametros
        if not self.initialized:
            raise PMYAPIException("Parametros no inicializados.")

        if not self.islogin:
            url = self.activeEndpoint + "auth/getToken"
            headers = {'X-Username': self.user, 'X-Password': self.password}
            login_response = requests.post(url, headers=headers, verify=self.verify_https)

            # Checkeamos si la respuesta del request fue correcta,
            # un ok va a ser un response code 200 (OK)
            if login_response.ok:
                self.token = login_response.headers['X-Auth-Token']
                success = True
            else:
                logging.warning("Error al autenticarnos...")
                success = False
            self.islogin = True
        else:
            logging.info("Ya estamos logueados")
            success = True

        return success
