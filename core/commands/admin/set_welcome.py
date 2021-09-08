from core import decorators
from core.utilities.message import message
from languages.getLang import languages
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import build_menu
import json

def _remove_button(group_id, btn_id):
    """ 
    group_id, int che indica l'id del gruppo
    btn_id, id del bottone json da rimuovere
    """
    # selezione
    group_record = GroupRepository().getById(group_id)
    welcome_btns = group_record['welcome_buttons']
    welcome_btns = json.loads(welcome_btns)['buttons']

    # rimozione
    welcome_btns = [ btn for btn in welcome_btns if btn['id'] != btn_id]

    # inserimento
    welcome_btns_text = json.dumps({"buttons": welcome_btns})
    GroupRepository().updateWelcomeButtonsByGroupId(group_id, welcome_btns_text)

def _add_button(group_id, btn):
    """ 
    group_id, int che indica l'id del gruppo
    btn, dict che rappresenta un bottone in json
    """
    # selezione
    group_record = GroupRepository().getById(group_id)
    welcome_btns = group_record['welcome_buttons']
    welcome_btns = json.loads(welcome_btns)['buttons']

    # aggiunta
    welcome_btns.append(btn)

    # inserimento
    welcome_btns_text = json.dumps({"buttons": welcome_btns})
    GroupRepository().updateWelcomeButtonsByGroupId(group_id, welcome_btns_text)

@decorators.admin.user_admin
@decorators.delete.init
def set_welcome_buttons(update, context):
    cmd_args = update.message.text[17:].strip().split()
    action = cmd_args[0]
    group_id = update.effective_chat.id
    
    if action == 'add':
        title = cmd_args[1][1:-1]
        url = cmd_args[2][1:-1]
        button = {'title': title, 'url': url}
        
        _add_button(group_id, button)

@decorators.admin.user_admin
@decorators.delete.init
def init(update, context):
    languages(update,context)
    record = GroupRepository.SET_WELCOME_TEXT
    chat = update.effective_chat.id
    msg = update.message.text[8:].strip()
    if msg != "":
        data = [(msg, chat)]
        GroupRepository().update_group_settings(record, data)
        message(update, context, languages.set_welcome_help)
    else:
        message(update, context, languages.set_welcome_main)


@decorators.admin.user_admin
@decorators.delete.init
def set_type_no_username(update, context):
    bot = context.bot
    chat = update.effective_message.chat_id
    buttons = []
    buttons.append(InlineKeyboardButton('Kick Only', callback_data='tpnu1'))
    buttons.append(InlineKeyboardButton('Message Only', callback_data='tpnu2'))
    buttons.append(InlineKeyboardButton('Mute Only', callback_data='tpnu3'))
    menu = build_menu(buttons,3)
    bot.send_message(chat,"No Username Filter Settings", reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')


@decorators.admin.user_admin
def update_set_tpnu(update, context):
    query = update.callback_query
    if query.data.startswith("tpnu"):
        chat_id = query.message.chat_id
        tpnu_set = query.data[4:]
        record = GroupRepository.SET_TPNU
        data = [(tpnu_set,chat_id)]
        GroupRepository().update_group_settings(record, data)
        text = "You have set the filter to <code>{}</code>\nLegend:\n<code>1 == Kick\n2 == Message\n3 == Mute</code>".format(tpnu_set)
        query.edit_message_text(text, parse_mode='HTML')
