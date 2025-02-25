#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
from core.commands import public ,admin, owner
from telegram.ext import (CommandHandler as CMH,CallbackQueryHandler as CQH)
from core.utilities.functions import close_menu

"""
MANUAL JOBS WITH /startjobs
"""
def core_jobs(update,context):
    pass
"""
Here are inserted all the commands with user permissions
"""
def user_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('start', public.start.init))
    function(CMH('help', public.help.init))
    function(CMH('rules', public.rules.init))
    function(CMH('io', public.io.init))
    function(CMH('source', public.source.init))
    function(CMH('report', public.report.global_report))
    function(CMH('lost', public.eggs.egg_lost))
    function(CMH('kickme', public.kickme.init))
    function(CMH('staff', public.staff.init))

"""
Here are inserted all the commands with admin permissions
"""
def admin_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('ban', admin.ban.init))
    function(CMH('unban', admin.unban.init))
    function(CMH('status', admin.info_group.init))
    function(CMH('lang', admin.set_lang.init))
    function(CMH('mute', admin.mute.init))
    function(CMH('check', admin.check_permission.init))
    function(CMH('warn', admin.warn.init))
    function(CMH('info', admin.user_info.init))
    function(CMH('say', admin.say.init))
    function(CMH('welcome', admin.set_welcome.init))
    function(CMH('settings', admin.settings.init))
    function(CMH('filters', admin.filters.init))
    function(CMH('setwarn', admin.warn.set_warn))
    function(CMH('setrules', admin.set_rules.init))
    function(CMH('setnousername', admin.set_welcome.set_type_no_username))
    function(CMH('usearch', admin.user_search.init))
    function(CMH('delete', admin.delete_message.init))
    function(CMH('welcomebuttons', admin.set_welcome.set_welcome_buttons))
    function(CMH('shield', admin.shield.init))
    function(CMH('badword', admin.badword.init))
    function(CMH('badlist', admin.badword.badlist))
    function(CMH('promote', admin.promote.init))
    function(CMH('chatid', admin.info_group.id_chat))
    #############################
    ### CallbackQuery Handler ###
    #############################
    function(CQH(owner.superban.update_superban, pattern='m'))
    function(CQH(close_menu, pattern='closeMenu'))
    function(CQH(owner.superban.update_superban, pattern='removeSuperban'))
    function(CQH(owner.whitelist.remove_blacklist, pattern='removeBL'))
    function(CQH(owner.whitelist.remove_blacklist, pattern='closed'))
    function(CQH(admin.warn.update_set_warn, pattern='w'))
    function(CQH(admin.warn.update_warn, pattern='upWarn'))
    function(CQH(admin.warn.update_warn, pattern='downWarn'))
    function(CQH(admin.warn.update_warn, pattern='removeWarn'))
    function(CQH(admin.set_welcome.update_set_tpnu, pattern='tpnu'))
    function(CQH(owner.add_community.callback_community, pattern='comm'))
    function(CQH(admin.mute.update_mute, pattern='CM'))
    function(CQH(admin.set_lang.language_en, pattern='language_en'))
    function(CQH(admin.set_lang.language_it, pattern='language_it'))
    function(CQH(admin.filters.update_filters, pattern='ff'))
    function(CQH(public.rules.update_rules, pattern='openRules'))
    function(CQH(public.report.update_resolve, pattern='resolved'))
    function(CQH(admin.shield.update_shield, pattern='removeShield'))
    function(CQH(admin.settings.update_settings))
"""
Here are inserted all the commands with owner permissions
"""
def owner_command(dsp):
    function = dsp.add_handler
    ######################
    ### CommandHandler ###
    ######################
    function(CMH('b', owner.broadcast.init, run_async=True))
    function(CMH('gb', owner.broadcast.global_broadcast, run_async=True))
    function(CMH('s', owner.superban.init, run_async=True))
    function(CMH('w', owner.whitelist.init))
    function(CMH('server', owner.server_info.init))
    function(CMH('community', owner.add_community.init))
    function(CMH('test', owner.test.init))
    function(CMH('owner', owner.add_owner.init))
    function(CMH('exit', owner.exit.init))
    function(CMH('startjobs', core_jobs))
    function(CMH('exportlink', owner.export_invite_link.init))