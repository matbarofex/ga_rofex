# -*- coding:utf8 -*-
"""
Configuration Module
"""

from connector_pmy_api.pmy_enums import Entorno
from enum import Enum
import os
import logging


LOGGING_LEVEL = logging.INFO if 'logging_level' not in os.environ else int(os.environ['logging_level'])


class PrimaryAPI:
    USER = os.environ['user_pmy_api']
    PASS = os.environ['pass_pmy_api']
    ENVIRONMENT = Entorno.PROD if 'env_pmy_api' not in os.environ else Entorno(int(os.environ['env_pmy_api']))


class Language(Enum):
    EN = 1
    ES = 2

class Markets(Enum):
    ROFEX = 1
    MATBA = 2

Instrument = {
    'Gold': {
        'name': {Language.EN: 'Gold', Language.ES: 'Oro'},
        'trade_months': [3, 5, 7, 9, 11],
        'initials': 'ORO',
        'market': Markets.ROFEX
    },
    'Oil': {
        'name': {Language.EN: 'Oil', Language.ES: 'Petróleo'},
        'trade_months': [5, 7, 9, 11],
        'initials': 'WTI',
        'market': Markets.ROFEX
    },
    'Dollar': {
        'name': {Language.EN: 'Dollar', Language.ES: 'Dólar'},
        'trade_months': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'initials': 'DO',
        'market': Markets.ROFEX
    },
    'Rofex Index': {
        'name': {Language.EN: 'ROFEX Index', Language.ES: 'Índice ROFEX'},
        'trade_months': [3, 6, 9, 12],
        'initials': 'RFX20',
        'market': Markets.ROFEX
    },
    'Spot Rofex': {
        'name': {Language.EN: 'ROFEX Index Spot', Language.ES : 'Spot Índice ROFEX'},
        'trade_months': [],
        'initials': 'I.RFX20',
        'market': Markets.ROFEX
    },
    'Soy': {
        'name': {Language.EN: 'Soybean', Language.ES: 'Soja'},
        'trade_months': [1, 3, 5, 6, 7, 9, 11],
        'initials': 'MATBA - ELEC - SOJ.ROS/',
        'market': Markets.MATBA,
        'related': ['Factory Soy', 'Mini Soy', 'Soy Index', 'Chicago Soy']
    },
    'Factory Soy': {
        'name': {Language.EN: 'Factory Soybean', Language.ES: 'Soja Fábrica'},
        'trade_months': [2, 4, 5, 7],
        'initials': 'MATBA - ELEC - SEF.ROS/',
        'market': Markets.MATBA
    },
    'Mini Soy': {
        'name': {Language.EN: 'Mini Soybean', Language.ES: 'Soja Mini'},
        'trade_months': [5, 7],
        'initials': 'MATBA - ELEC - SOJ.MIN/',
        'market': Markets.MATBA
    },
    'Soy Index': {
        'name': {Language.EN: 'ROSAFE Soybean Index', Language.ES: 'Índice Soja ROSAFÉ'},
        'trade_months': [5, 7],
        'initials': 'MATBA - ELEC - ISR/',
        'market': Markets.MATBA
    },
    'Chicago Soy': {
        'name': {Language.EN: 'Chicago Soybean', Language.ES: 'Soja Chicago'},
        'trade_months': [2, 4, 6],
        'initials': 'MATBA - ELEC - SOY.CME/',
        'market': Markets.MATBA
    },
    'Corn': {
        'name': {Language.EN: 'Corn', Language.ES: 'Maíz'},
        'trade_months': [2, 3, 4, 6, 7, 9, 12],
        'initials': 'MATBA - ELEC - MAI.ROS/',
        'market': Markets.MATBA,
        'related': ['Mini Corn', 'Chicago Corn']
    },
    'Mini Corn': {
        'name': {Language.EN: 'Mini Corn', Language.ES: 'Maíz Mini'},
        'trade_months': [4, 7],
        'initials': 'MATBA - ELEC - MAI.MIN/',
        'market': Markets.MATBA
    },
    'Chicago Corn': {
        'name': {Language.EN: 'Chicago Corn', Language.ES: 'Maíz Chicago'},
        'trade_months': [2, 4, 6, 8],
        'initials': 'MATBA - ELEC - CRN.CME/',
        'market': Markets.MATBA
    },
    'Wheat': {
        'name': {Language.EN: 'Wheat', Language.ES: 'Trigo'},
        'trade_months': [1, 2, 3, 4, 7, 10, 12],
        'initials': 'MATBA - ELEC - TRI.ROS/',
        'market': Markets.MATBA,
        'related': ['Buenos Aires Wheat', 'Mini Wheat']
    },
    'Buenos Aires Wheat': {
        'name': {Language.EN: 'Buenos Aires Wheat', Language.ES: 'Trigo Buenos Aires'},
        'trade_months': [2, 3, 5, 7, 9],
        'initials': 'MATBA - ELEC - TRI.BA/',
        'market': Markets.MATBA
    },
    'Mini Wheat': {
        'name': {Language.EN: 'Mini Wheat', Language.ES: 'Trigo Mini'},
        'trade_months': [1, 7],
        'initials': 'MATBA - ELEC - TRI.MIN/',
        'market': Markets.MATBA
    }
}

Month = {
    '1': {'initials': {Markets.ROFEX: 'Ene', Markets.MATBA: 'ENE'}, 'text': {Language.EN: 'January', Language.ES: 'Enero'}},
    '2': {'initials': {Markets.ROFEX: 'Feb', Markets.MATBA: 'FEB'}, 'text': {Language.EN: 'February', Language.ES: 'Febrero'}},
    '3': {'initials': {Markets.ROFEX: 'Mar', Markets.MATBA: 'MAR'}, 'text': {Language.EN: 'March', Language.ES: 'Marzo'}},
    '4': {'initials': {Markets.ROFEX: 'Abr', Markets.MATBA: 'ABR'}, 'text': {Language.EN: 'April', Language.ES: 'Abril'}},
    '5': {'initials': {Markets.ROFEX: 'May', Markets.MATBA: 'MAY'}, 'text': {Language.EN: 'May', Language.ES: 'Mayo'}},
    '6': {'initials': {Markets.ROFEX: 'Jun', Markets.MATBA: 'JUN'}, 'text': {Language.EN: 'June', Language.ES: 'Junio'}},
    '7': {'initials': {Markets.ROFEX: 'Jul', Markets.MATBA: 'JUL'}, 'text': {Language.EN: 'July', Language.ES: 'Julio'}},
    '8': {'initials': {Markets.ROFEX: 'Ago', Markets.MATBA: 'AGO'}, 'text': {Language.EN: 'August', Language.ES: 'Agosto'}},
    '9': {'initials': {Markets.ROFEX: 'Sep', Markets.MATBA: 'SEP'}, 'text': {Language.EN: 'September', Language.ES: 'Septiembre'}},
    '10': {'initials': {Markets.ROFEX: 'Oct', Markets.MATBA: 'OCT'}, 'text': {Language.EN: 'October', Language.ES: 'Octubre'}},
    '11': {'initials': {Markets.ROFEX: 'Nov', Markets.MATBA: 'NOV'}, 'text': {Language.EN: 'November', Language.ES: 'Noviembre'}},
    '12': {'initials': {Markets.ROFEX: 'Dic', Markets.MATBA: 'DIC'}, 'text': {Language.EN: 'December', Language.ES: 'Diciembre'}},
}

Entries = {
    'Last Price': {'text': {Language.EN: 'Last Price', Language.ES: 'Último Precio'}, 'symbol': 'LA', 'side': 'price'},
    'Settlement Price': {'text': {Language.EN: 'Settlement Price', Language.ES: 'Precio de Ajuste'}, 'symbol': 'SE', 'side': 'price'},
    'Effective Volume': {'text': {Language.EN: 'Effective Volume', Language.ES: 'Volumen Efectivo'}, 'symbol': 'EV', 'side': 'price'},
    'Nominal Volume': {'text': {Language.EN: 'Nominal Volume', Language.ES: 'Volumen Nominal'}, 'symbol': 'NV', 'side': 'price'},
    'Open Interest': {'text': {Language.EN: 'Open Interest', Language.ES: 'Interés Abierto'}, 'symbol': 'OI', 'side': 'size'},
    'Default': {'symbol': 'LA,SE'}
}