# pylint: disable=unused-argument

from telegram import Update
from telegram.ext import ContextTypes

from commands.other_commands import callback_not_realized_yet
from keyboards import SECOND_STATE_KEYBOARD
from settings import ORDERS_TEXT, SECOND_STATE


async def orders(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    reply_markup = SECOND_STATE_KEYBOARD
    await query.message.reply_text(
        text=ORDERS_TEXT, reply_markup=reply_markup
    )
    return SECOND_STATE


async def become_partner(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await callback_not_realized_yet(update, context)
