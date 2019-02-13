<h1>ROFEX for GOOGLE ASSISTANT</h1>

version : 1.0.0

#### Intro

This project contains the code for a web service deployed in a Google Function that receive a POST request from ROFEX Dialogflow Agent. 

The main function allow user to request prices of ROFEX instruments. The Intent that trigger the price response is the LastPriceIntent.

#### Configuration

Configuration variables are set in the _`configuration/config.py`_ module.

As this is intent to be used in a Google Function, the parameters are set as Environment Variables of the function:

- `user_pmy_api`: username for Primary API </br>
- `pass_pmy_api`: password for Primary API </br>
**Optionally**:
- `env_pmy_api`: Number that specify Environment of Primary API used. 1 for Demo; 2 for Production; 3 for Remarket. Default: Production Environment.
- `logging_level`: Number that specify logging level to use (see https://goo.gl/35Lwkr for more info). Default: INFO.
 
You'll need to have valid Primary API credential in order to authenticate and request prices to the API. 

#### How it work
The main entry point for the Function is the `agent_fulfillment_handler` function in the _`main.py`_ module.

In the `_ga_handler_` folder you will find Handler Class for DialogFlow Requests. The only implementation is GAForRFXHandler that contain all the logic to process user's requests and return appropriate response.

The modules in _`connector_pmy_api`_ folder are use to establish the connection to Primary API and request market data.

#### Support
Developer: Primary S.A.

Contact: mpi@primary.com.ar