import logging
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError)
from core.utilities.message import messageWithId


def init(update, context):
    txt = update.message.text
    err = '[error]'
    try:
        raise context.error
    except Unauthorized:
        err = '🔴 <b>[ERROR]:</b> <code>Unauthorized</code>\n'
        #error_message(update, context, err)
        # remove update.message.chat_id from conversation list
    except BadRequest:
        err = '🔴 <b>[ERROR]:</b> <code>BadRequest - malformed requests</code>\n'
        #error_message(update, context, err)
        # handle malformed requests - read more below!
    except TimedOut:
        err = '🔴 <b>[ERROR]:</b> <code>TimedOut - slow connection problems</code>\n'
        #error_message(update, context, err)
        # handle slow connection problems
    except NetworkError:
        err = '🔴 <b>[ERROR]:</b> <code>NetworkError - other connection problems</code>\n'
        #error_message(update, context, err)
        # handle other connection problems
    except ChatMigrated:
        err = '🔴 <b>[ERROR]:</b> <code>ChatMigrated - chat_id not found (maybe group/channel migrated?)</code>\n'
        #error_message(update, context, err)
        # the chat_id of a group has changed, use e.new_chat_id instead
    except TelegramError:
        err = '🔴 <b>[ERROR]:</b> <code>TelegramError\nThis is a generic error not handled by other handlers, check the console logs for info</code>\n'
        #error_message(update, context, err)
        # handle all other telegram related errors
    except AttributeError:
        err = '🔴 <b>[ERROR]:</b> <code>AttributeError -  bad code</code>'
    except TypeError:
        # err = '[ERROR] TypeError - Unknown'
        # need to fix this...
        err = None

    if err != None:
        error_message(update, context, err, txt)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
def error_message(update, context, err, txt):
    chat_id = -1001267698171
    log = '\n🔵 <b>[LOG_ERROR]:</b> <code>{}</code>'.format(context.error)
    txt = "🤖 Bot Command: {}\n\n{}{}".format(txt, err, log)
    messageWithId(update,context,chat_id,txt)