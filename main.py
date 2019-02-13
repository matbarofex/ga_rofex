import logging
from flask import abort
from configuration.config import LOGGING_LEVEL
from ga_handlers.GAForRFXHandler import GAForRFXHandler

"""
Main entry point for DialogFlow Fulfillment request.
"""


logging.basicConfig(format='%(asctime)s %(message)s')
logging.getLogger().setLevel(LOGGING_LEVEL)


def agent_fulfillment_handler(request):

    logging.info("Executing agent_fulfillment_handler...")

    # Only process POST method
    if request.method == 'POST':
        # Create GA Handler to process the request
        ga = GAForRFXHandler()
        return ga.process_request(request.get_json(silent=True, force=True))
    else:
        return abort(405)
