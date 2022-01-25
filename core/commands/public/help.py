#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.utilities.menu import build_menu
from languages.getLang import languages
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def init(update,context):
    bot = context.bot
    chat = update.effective_message.chat_id
    languages(update,context)
    msg = languages.helps.format("@"+bot.username)
    buttons = []
    buttons.append(InlineKeyboardButton("Lista Comenzi", url='https://github.com/Squirrel-Network/nebula8/wiki/Command-List'))
    buttons.append(InlineKeyboardButton("Traducere", url='https://t.me/OTRportal/'))
    buttons.append(InlineKeyboardButton("Canal LOG", url='https://t.me/+axTHOyJqhVBjN2Nk'))
    buttons.append(InlineKeyboardButton("Grupuri RO", url='https://t.me/GrupuriRomanesti'))
    buttons.append(InlineKeyboardButton("Secret", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    buttons.append(InlineKeyboardButton("Official", url='https://t.me/HaitaLupilor'))
    buttons.append(InlineKeyboardButton("H.A.I.T.A.🐺🎭😍⚔❤", url='https://t.me/LupiiDinHaita'))
    menu = build_menu(buttons,3)
    bot.send_message(chat,msg,reply_markup=InlineKeyboardMarkup(menu))
