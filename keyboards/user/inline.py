from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData


async def start_keyboard():

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton(
            text='Отдел контрольно-пропускного режима',
            callback_data='1'
        ),
        InlineKeyboardButton(
            text='Воинский учет (2 отдел)',
            callback_data='2'
        ),
        InlineKeyboardButton(
            text='Медпункт',
            callback_data='3'
        ),
        InlineKeyboardButton(
            text='Социальная стипендия',
            callback_data='4'
        ),
        InlineKeyboardButton(
            text='Общежития',
            callback_data='5'
        ),
        InlineKeyboardButton(
            text='Институты',
            callback_data='6'
        ),
        InlineKeyboardButton(
            text='БСК',
            callback_data='7'
        ),
        InlineKeyboardButton(
            text='Библиотека',
            callback_data='8'
        ),
        InlineKeyboardButton(
            text='Отдел кадров',
            callback_data='9'
        ),
        InlineKeyboardButton(
            text='Как получить справку',
            callback_data='10'
        ),

    )

    return markup

async def menu_keyboard():

    markup = InlineKeyboardMarkup(row_width=2)

    markup.add(
        InlineKeyboardButton(
            text='Назад',
            callback_data='back'
        )
    )

    return markup