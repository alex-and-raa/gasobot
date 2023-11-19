from telegram import Update
from telegram.ext import ConversationHandler, ContextTypes

from settings import UNKNOWN_COMMAND, NOT_REALIZED_YET


async def callback_not_realized_yet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=NOT_REALIZED_YET)
    return ConversationHandler.END


async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.callback_query:
        await update.callback_query.answer()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=UNKNOWN_COMMAND)
