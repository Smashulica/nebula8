import re
from core import decorators
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from core.database.repository.user import UserRepository
from core.database.repository.superban import SuperbanRepository
from core.utilities.message import message, reply_message
from core.utilities import functions
from core.utilities.functions import delete_message
from telegram.ext.dispatcher import run_async
from core.utilities.functions import kick_user, ban_user

def has_arabic_character(string):
    arabic = re.search("[\u0600-\u06ff]|[\u0750-\u077f]|[\ufb50-\ufbc1]|[\ufbd3-\ufd3f]|[\ufd50-\ufd8f]|[\ufd92-\ufdc7]|[\ufe70-\ufefc]|[\uFDF0-\uFDFD]+", string)
    return not not arabic

def save_user(user):
    # Salva l'utente nel database e controlla che esiste se esiste e ha cambiato nickname sovrascrivi
    user = UserRepository.getById(user.id)
    if user:
        UserRepository.update(username = user.username)
    else:
        UserRepository.add(user)

def is_in_blacklist(uid):
    return not not SuperbanRepository.getByIdFetchOne(uid)

def welcome_user(update, context, member):
    # Controlla che il welcome esista sul database se non esiste Default Welcome
    chat = update.effective_message.chat_id

    groups = GroupRepository().getById(chat)
    if groups is not None:
        group = groups[0]

        parsed_message = group['welcome_text'].replace(
            '{first_name}',
            update.message.from_user.first_name).replace('{chat_name}',
            update.message.chat.title).replace('{username}',
            "@"+member.username
        )
        format_message = "{}".format(parsed_message)
        # welcome = update.message.reply_text(format_message,parse_mode='HTML')
        reply_message(format_message)
    else:
        reply_message('default welcome')


def welcome_bot(update, context):
    # TODO: handler che salva il gruppo suò database e controlla che esiste. se esiste e ha cambiato id lo cambia
    reply_message(update, context, "Grazie per avermi aggiunta al gruppo :D")

@run_async
def init(update, context):
    for member in update.message.new_chat_members:
        print('***Welcome*** ' + str(member))

        if member.is_bot:
            print('***Welcome*** ' + 'is_bot')
            welcome_bot(update, context)

        else:
            print('***Welcome*** ' + 'is_user')
            # save_user(member)

            if member.username is None:
                print('***Welcome*** ' + 'no username')
                kick_user(update, context)

            # TODO: add flag blacklist active
            elif is_in_blacklist(member.id) or has_arabic_character(member.username):
                print('***Welcome*** ' + 'blacklist or arabic')
                ban_user(update, context)

            else:
                print('***Welcome*** ' + 'welcome')
                welcome_user(update, context, member)
