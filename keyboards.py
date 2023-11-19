from telegram import InlineKeyboardMarkup, InlineKeyboardButton

FIRST_STATE_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("О компании", callback_data="about_company"),
            InlineKeyboardButton("Уровень добычи", callback_data="production_level"),
        ],
        [InlineKeyboardButton("Заказы", callback_data="orders")]
    ]
)

SECOND_STATE_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Стать партнером", callback_data="become_partner"),
            InlineKeyboardButton("Отследить договор", callback_data="check_contract"),
        ]
    ]
)

THIRD_STATE_KEYBOARD = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Посмотреть", callback_data="look_contract"),
            InlineKeyboardButton("Изменить", callback_data="change_contract"),
            InlineKeyboardButton("Расторгнуть", callback_data="terminate_contract"),
        ]
    ]
)
