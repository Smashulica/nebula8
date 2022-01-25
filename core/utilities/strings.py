#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

class Strings(object):
    ERROR_HANDLING = "A aparut o eroare incercand sa rulez aceasta comanda.\nTe rog sa soliciti support folosind comanda /report"
    BAN_LOG = "<b>⚠️ #Log Utilizator Banat!</b>\n👤 ID: {id}\n"\
              '👤 Username: <a href="tg://user?id={id}">{username}</a>\n'\
              "👥 Grup: {chat}\n"
    SUPERBAN_LOG = '<b>🚷 #Log User Global BAN!</b>\n👤 ID: [{}]\n📜 Motiv: {}\n🕐 Data si ora: <code>{}</code>\n👮‍♀️ Cine la banat: {} [{}]'
    REPORT_MSG = "⚠️ #Report\nGroup Id: <code>{}</code>\nGroup Title: {}\nMessage: <i>{}</i>\n📎 Link: {}"
    SOURCE = "<b>Salut/Buna! numele meu este: {}\nVersiunea mea este: <code>{} {}</code>\nMy group: @LupiiDinHaita {}</b>"
    USER_INFO = '<b>⚙️ INFO USER:</b>\n👤 ID: <code>{id}</code>\n👤 Username: <a href="tg://user?id={id}">{username}</a>\n⚠️ Warnuri: <code>{warn}</code>\n👥 Grup: {chat}'
    WELCOME_BOT = "Thanks for adding me to the group\nPlease select your language => /lang\n\nRemember to make me administrator to work properly!\n\nNeed Help? => /help\n\nTo change the group settings, press the /settings command\nTo change the filters in the group, type /filters\nMy Version is: {} {}"
