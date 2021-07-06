#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG | @Hillard_Har  

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from  bot.__init__ import BOT_NAME, ADMIN_USERNAME, GROUP_USERNAME
from bot import FORCESUB_CHANNEL

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
#adding force subscribe option to bot
    update_channel = FORCESUB_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("🤭 Sorry Dude, You are **B A N N E D 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{BOTS_Infinity} To Use Me")
            await update.reply_text(
                text=""" <b> ⚠️ YOU ARE NOT SUBSCRIBED OUR CHANNEL⚠️

Join on our channel to get movies ✅


⚠️താങ്കൾ ഞങ്ങളുടെ ചാനൽ സബ്സ്ക്രൈബ് ചെയ്തിട്ട് ഇല്ല ! ⚠️


ഞങ്ങളുടെ ചാനലിൽ ജോയിൻ ചെയ്യതാൽ താങ്കൾക്ക് movies കിട്ടുന്നത് ആണ് ✅

⬇️Channel link⬇️ </b>""",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="⚡ Join My Channel⚡️", url=f"https://t.me/{BOTS_Infinity}")]
              ])
            )
            return
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📫 SUPPORT', url="https://t.me/BOTS_Infinity"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📫 SUPPORT', url="https://t.me/BOTS_Infinity"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '📫 SUPPORT', url="https://t.me/BOTS_Infinity"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('📫 SUPPORT', url='https://t.me/BOTS_Infinity'),
        InlineKeyboardButton('📕 ABOUT', callback_data="about")
    ],[
        InlineKeyboardButton('💡 HELP', callback_data="help"),
        InlineKeyboardButton('🔐 CLOSE', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.first_name, GROUP_USERNAME, ADMIN_USERNAME),
        reply_markup=reply_markup,
        parse_mode="html"
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('⬇️ BACK', callback_data='start'),
        InlineKeyboardButton('🔐 CLOSE', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html", 
        disable_web_page_preview=True
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('⬇️ BACK', callback_data='start'),
        InlineKeyboardButton('🔐 CLOSE', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT.format(BOT_NAME),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="markdown"
    )
