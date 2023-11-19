# pylint: disable=unused-argument

from telegram import Update
from telegram.ext import ContextTypes

from keyboards import FIRST_STATE_KEYBOARD
from settings import GREETINGS_TEXT, OPTIONS_FIRST_TEXT, OPTIONS_FURTHER_TEXT, ABOUT_COMPANY_TEXT, \
    PRODUCTION_LEVEL_TEXT, FIRST_STATE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(text=GREETINGS_TEXT)
    return await options(update, context)

#вызов кнопок выбора (клавиатура)
async def options(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    reply_markup = FIRST_STATE_KEYBOARD
    if update.message:
        # after "/start" command
        await update.message.reply_text(text=OPTIONS_FIRST_TEXT, reply_markup=reply_markup)
    elif update.callback_query:
        # proceeding callback
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(text=OPTIONS_FURTHER_TEXT, reply_markup=reply_markup)

    return FIRST_STATE


async def about_company(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(text=ABOUT_COMPANY_TEXT)
    return await options(update, context)


async def production_level(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(text=PRODUCTION_LEVEL_TEXT)
    return await options(update, context)
