# pylint: disable=unused-argument

from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from commands.first_stage_commands import options
from commands.third_stage_commands import check_contract
from db_connection import view_contract
from exceptions import NotFoundInDatabase
from settings import FOURTH_STATE, LOOK_CONTRACT_TEXT, LOOK_PARTICULAR_CONTRACT_NOT_FOUND_TEXT


async def look_contract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(text=LOOK_CONTRACT_TEXT)
    return FOURTH_STATE


async def look_particular_contract(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    contract_number = update.message.text
    try:
        contract_info = view_contract(contract_number)
        contract_info_parsed = _parse_contract(contract_info)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=contract_info_parsed)
        return await options(update, context)
    except NotFoundInDatabase:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=LOOK_PARTICULAR_CONTRACT_NOT_FOUND_TEXT)
        return await check_contract(update, context)


def _parse_contract(contract_info: dict[str, str]) -> str:
    contract_info_rus = {
        "Номер договора": contract_info["contract_number"],
        "Статус договора": contract_info["status"],
        "Клиент по договору": contract_info["contract_client"],
        "Дата подписания договора": contract_info["sign_date"],
        "Дата окончания действия договора": contract_info["expire_date"]
    }
    contract_info_list = []
    for key, value in contract_info_rus.items():
        contract_info_list.append(f'{key}: {value}')
    contract_info_parsed = '\n'.join(contract_info_list)
    return contract_info_parsed
