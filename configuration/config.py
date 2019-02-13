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

Instrument = {
    'Soy': {
        'name': {Language.EN: 'soy', Language.ES: 'soja'},
        'trade_months': [5, 11],
        'initials': 'S'
    },
    'Gold': {
        'name': {Language.EN: 'gold', Language.ES: 'oro'},
        'trade_months': [3, 5, 7, 9, 11],
        'initials': 'ORO'
    },
    'Oil': {
        'name': {Language.EN: 'oil', Language.ES: 'petróleo'},
        'trade_months': [3, 5, 7, 9, 11],
        'initials': 'WTI'
    },
    'Dolar': {
        'name': {Language.EN: 'Dollar', Language.ES: 'Dólar'},
        'trade_months': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'initials': 'DO'
    },
    'Rofex Index': {
        'name': {Language.EN: 'ROFEX Index', Language.ES: 'Índice ROFEX'},
        'trade_months': [3, 6, 9, 12],
        'initials': 'RFX20'
    },
    'Spot Rofex': {
        'name': {Language.EN: 'ROFEX Index Spot', Language.ES : 'Spot Índice ROFEX'},
        'trade_months': [],
        'initials': 'I.RFX20'
    }
}

Month = {
    '1': {'initials': 'Ene', 'text': {Language.EN : 'january', Language.ES : 'enero'}},
    '2': {'initials': 'Feb', 'text': {Language.EN : 'february', Language.ES : 'febrero'}},
    '3': {'initials': 'Mar', 'text': {Language.EN : 'march', Language.ES : 'marzo'}},
    '4': {'initials': 'Abr', 'text': {Language.EN : 'april', Language.ES : 'abril'}},
    '5': {'initials': 'May', 'text': {Language.EN : 'may', Language.ES : 'mayo'}},
    '6': {'initials': 'Jun', 'text': {Language.EN : 'june', Language.ES : 'junio'}},
    '7': {'initials': 'Jul', 'text': {Language.EN : 'july', Language.ES : 'julio'}},
    '8': {'initials': 'Ago', 'text': {Language.EN : 'august', Language.ES : 'agosto'}},
    '9': {'initials': 'Sep', 'text': {Language.EN : 'september', Language.ES : 'septiembre'}},
    '10': {'initials': 'Oct', 'text': {Language.EN : 'october', Language.ES : 'octubre'}},
    '11': {'initials': 'Nov', 'text': {Language.EN : 'november', Language.ES : 'noviembre'}},
    '12': {'initials': 'Dic', 'text': {Language.EN : 'december', Language.ES : 'diciembre'}},
}

