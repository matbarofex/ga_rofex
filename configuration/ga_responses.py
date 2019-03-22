# coding: utf-8
import configuration.config as conf

LANG_NOT_SUPPORTED = {
    conf.Language.EN : "Sorry, I don't recognize this language."
}

INIT_RESPONSE = {
    conf.Language.EN : "Welcome to ROFEX Assistant. "
                       "Please, tell me an instrument and I'll give you the last price available for the contract. "
                       "If you need help asking me questions just say 'HELP'",
    conf.Language.ES : "Bienvenidos al Asistente de ROFEX. "
                       "Por favor, dime un instrumento y te diré el último precio disponible para ese contrato. "
                       "Si necesitas ayuda solo dí 'AYUDA'"
}

DEFAULT_RESPONSE = {
    conf.Language.EN : "Sorry, I didn't get that. Can you say it again?",
    conf.Language.ES : "Perdón, no entendí eso. ¿Podrías repetirlo?"
}


ASK_INSTRUMENT_RESPONSE = {
    conf.Language.EN: "Please, tell me the instrument you want to know.",
    conf.Language.ES: "Por favor, dime el instrumento que deseas saber."
}

ERROR_RESPONSE = {
    conf.Language.EN : "Sorry, an error has occurred and I couldn't process your request. "
                       "Please, ask me again.",
    conf.Language.ES : "Lo siento, ocurrió un error y no pude procesar tu consulta. "
                       "Por favor, intentalo de nuevo."
}

LAST_PRICE_OK_RESPONSE = {
    conf.Language.EN : "The price for {0} future {1} contract is {2}. Want to try it again?",
    conf.Language.ES : "El precio para el futuro de {0} posición {1} es {2}. ¿Quieres consultarme otro instrumento?"
}

LAST_PRICE_OK_RESPONSE_SPOT = {
    conf.Language.EN : "The price for {0} is {1}. Want to try it again?",
    conf.Language.ES : "El precio para el {0} es {1}. ¿Quieres consultarme otro instrumento?"
}

ENTRY_PRICE_OK_RESPONSE = {
    conf.Language.EN : "{0} for {1} future {2} contract is {3}. Want to try it again?",
    conf.Language.ES : "El {0} para el futuro de {1} posición {2} es {3}. ¿Quieres consultarme otro instrumento?"
}

LAST_PRICE_ERROR_RESPONSE = {
    conf.Language.EN : "Sorry, {0} is not a valid instrument. Please ask me again.",
    conf.Language.ES : "Perdón, {0} no es un instrumento válido. Por favor, preguntame de nuevo."
}

LAST_PRICE_INSTRUMENT_NOT_FOUND_RESPONSE = {
    conf.Language.EN : "I could not find a valid contract for {0} future {1} contract. "
                       "The most recent position for this instrument is {2}. "
                       "Please try again with this position.",
    conf.Language.ES : "El futuro de {0} no posee una posición abierta para {1}. "
                       "La posición más reciente para este instrumento es {2}. "
                       "Por favor, intenta de vuelta con esa posición."
}

LAST_PRICE_MD_NOT_FOUND_RESPONSE = {
    conf.Language.EN : "Sorry, there is no data available for this instrument now. "
                       "Want to try it with another instrument?",
    conf.Language.ES : "Perdón, no hay información disponible para este instrumento en este momentos. "
                       "¿Quieres intentarlo con otro instrumento?"
}

ENTRY_PRICE_MD_NOT_FOUND_RESPONSE = {
    conf.Language.EN : "Sorry, {0} is not available for this instrument now. "
                       "Please, try again with another data or instrument.",
    conf.Language.ES : "Perdón, en este momento no hay {0} disponible para este instrumento. "
                       "Por favor, intentalo de nuevo con otro dato o instrumento."
}

END_RESPONSE = {
    conf.Language.EN : "Thank you! Have a nice day.",
    conf.Language.ES : "Nos vemos pronto!"
}

API_UNAVAILABLE_RESPONSE = {
    conf.Language.EN : "Sorry, Primary service is not available right now. Please try again later.",
    conf.Language.ES : "Lo siento, el servicio de Primary no esta disponible en estos momentos. "
                       "Por favor, intentalo de nuevo más tarde."
}

###############################################################################################
###############################################################################################
# 1 - Help Possibilities
HELP_RESPONSE = {
    conf.Language.EN : "Ok, if you want to know how to ask the price of an instrument, "
                       "say 'Question' and I'll help you. "
                       "Also, I can tell you the list of valid instruments, "
                       "just say 'Instruments', "
                       "and to know the list of the available data of "
                       "the instruments, say 'Instruments Data'. "
                       "Want to try it?",
    conf.Language.ES : "Esta bien, si quieres saber como preguntarme el precio de un instrumento, "
                       "dime 'Preguntar' y te ayudaré. "
                       "También te puedo decir la lista de instrumentos válidos, "
                       "solo dí 'Instrumentos', "
                       "y para conocer la lista de datos disponibles sobre "
                       "los instrumentos, dí 'Datos de Instrumentos'. "
                       "¿Quieres intentarlo?"
}

# 1.1 - Question Response
QUESTION_RESPONSE = {
    conf.Language.EN : "To know the price of an instrument just tell me "
                       "the instrument's name and, optionally, "
                       "the month of the contract. Additionally, "
                       "you could specify the market data you want to know. "
                       "Want to try it?",
    conf.Language.ES : "Para saber el precio de un instrumento solo tienes que "
                       "decirme el nombre del instrumento y, opcionalmente, "
                       "el mes del contrato. Adicionalmente, puedes especificar "
                       "el dato de mercado que deseas saber. "
                       "¿Quieres intentarlo?"
}

# 1.2 - Instruments List Response
INSTRUMENT_LIST_RESPONSE = {
    conf.Language.EN : "You can ask me for the following instruments: "
                       "Dollar: for dollar futures. "
                       "ROFEX Index: for ROFEX 20 Index futures. "
                       "Gold: for gold futures. "
                       "Oil: for oil futures. "
                       "Soybean: for soybean futures. "
                       "Corn: for corn futures. "
                       "Wheat: for wheat futures. "
                       "If you want more details about any instrument "
                       "just say 'Help' and the name of the instrument. "
                       "Want to try it?",
    conf.Language.ES : "Puedes consultarme los siguientes instrumentos: "
                       "Dólar: para futuros de dólar. "
                       "Índice ROFEX: para futuros sobre el Índice ROFEX 20. "
                       "Oro: para futuros de oro. "
                       "Petróleo: para futuros de petróleo. "
                       "Soja: para futuros de soja. "
                       "Maíz: para futuros de maíz. "
                       "Trigo: para futuros de trigo. "
                       "Si quieres saber más detalles acerca de algún instrumento "
                       "solo dí 'Ayuda' y el nombre del instrumento. "
                       "¿Quieres intentarlo?"
}

# 1.2.1 - Instruments Detailed Response
HELP_RELATED_INST_RESPONSE = {
    conf.Language.EN : "Ok, when you mention the instrument '{0}', I will tell you "
                       "the last price available for the contract. "
                       "Also, let me tell you that there are other {0} "
                       "related instruments, like: {1}. "
                       "Just tell me the instrument full name and I will tell you the price. "
                       "Want to try it?",
    conf.Language.ES : "Bien, cuando menciones el instrumento '{0}' te diré el "
                       "último percio disponible para ese contrato. "
                       "También puedes consultar otros instrumentos relacionados con {0} como: {1}. "
                       "Solo dí el nombre del instrumento completo y te dire el precio. "
                       "¿Quieres intentarlo?"
}

# 1.2.2 - Instruments Detailed Response Default
HELP_INSTRUMENT_RESPONSE = {
    conf.Language.EN : "Ok, when you mention the instrument '{0}', I will tell you "
                       "the last price available for the contract. For example, to know the "
                       "price of {0} future June contract, just say '{0} June'. "
                       "Want to try it?",
    conf.Language.ES : "Bien, cuando menciones el instrumento '{0}' te diré el "
                       "último percio disponible para ese contrato. Por ejemplo, para saber "
                       "el precio del futuro sobre {0} posición Junio, solo tienes que decir "
                       "'{0} Junio'."
                       "¿Quieres intentarlo?"
}


# 1.3 - Entry List
ENTRY_LIST_RESPONSE = {
    conf.Language.EN : "When asking for an instrument you could also "
                       "specify the market data you want to know about. "
                       "Now, the available data are: "
                       "Last Price, Settlement Price, Effective Volume, "
                       "Nominal Volume and Open Interest. "
                       "Want to try it?",
    conf.Language.ES : "Al consultar un instrumento también puedes especificar "
                       "el dato de mercado que deseas saber. "
                       "Por ahora, los datos disponibles son: "
                       "Último Precio, Precio de Ajuste, Volumen Efectivo, "
                       "Volumen Nominal e Interés Abierto. "
                       "¿Quieres intentarlo?"
}
