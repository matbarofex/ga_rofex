# coding: utf-8
import configuration.config as conf

LANG_NOT_SUPPORTED = {
    conf.Language.EN : "Sorry, I don't recognize this language."
}

INIT_RESPONSE = {
    conf.Language.EN : "Welcome to ROFEX Assistant. Which instrument do you want to consult? "
                       "If you need help asking me questions just say 'HELP'",
    conf.Language.ES : "Bienvenidos al Asistente de ROFEX. ¿Que instrumento deseas consultar? "
                       "Si necesitas ayuda solo dí 'AYUDA'"
}

DEFAULT_RESPONSE = {
    conf.Language.EN : "Sorry, I didn't get that. Can you say it again?",
    conf.Language.ES : "Perdón, no entendí eso. ¿Podrías repetirlo?"
}

HELP_RESPONSE = {
    conf.Language.EN : "If you want to know the last price of ROFEX future contract, "
                       "just tell me the instrument's name, and optionally, "
                       "the month of the contract. Also, if you need the list of valid "
                       "instruments, said the word 'Instruments' and I'll tell you. "
                       "Want to try it?",
    conf.Language.ES : "Si quieres saber el último precio de un futuro en ROFEX, "
                       "solo tienes que decirme el nombre del instrumento, "
                       "y opcionalmente, el mes del contrato. También te puedo decir los instrumentos "
                       "que me puedes consultar, solo dí la palabra 'Instrumentos' y te ayudaré. "
                       "¿Quieres intentarlo?"
}

LIST_RESPONSE = {
    conf.Language.EN : "You can ask me for the following instruments: "
                       "Dollar: for dollar futures. "
                       "ROFEX Index: for ROFEX 20 Index futures. "
                       "Gold: for gold futures. "
                       "Oil: for oil futures. "
                       "Soy: for soy futures. "
                       "Want to try it?",
    conf.Language.ES : "Puedes consultarme los siguientes instrumentos: "
                       "Dólar: para futuros de dólar. "
                       "Índice ROFEX: para futuros sobre el índice ROFEX 20. "
                       "Oro: para futuros de oro. "
                       "Petróleo: para futuros de petróleo. "
                       "Soja: para futuros de soja. "
                       "¿Quieres intentarlo?"
}

ERROR_RESPONSE = {
    conf.Language.EN : "Sorry, an error has occurred and I couldn't process your request. "
                       "Please, ask me again.",
    conf.Language.ES : "Lo siento, ocurrió un error y no pude procesar tu consulta. "
                       "Por favor, intentalo de nuevo."
}

LAST_PRICE_OK_RESPONSE = {
    conf.Language.EN : "Last price for {0} future {1} contract is {2}. Want to try it again?",
    conf.Language.ES : "El último precio para el futuro de {0} posición {1} es {2}. ¿Quieres consultarme otro instrumento?"
}

LAST_PRICE_OK_RESPONSE_SPOT = {
    conf.Language.EN : "Last price for {0} is {1}. Want to try it again?",
    conf.Language.ES : "El último precio para el {0} es {1}. ¿Quieres consultarme otro instrumento?"
}

SETTLE_PRICE_OK_RESPONSE = {
    conf.Language.EN : "There is no last price available for {0} future {1} contract. "
                       "Although, the settlement price for this contract is {2}. "
                       "Want to try it again?",
    conf.Language.ES : "No hay último precio disponible para el futuro de {0} posición {1}. "
                       "El precio de ajuste para ese contrato es {2}. "
                       "¿Quieres consultarme otro instrumento?"
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
