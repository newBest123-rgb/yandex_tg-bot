from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ib_1 = InlineKeyboardButton(text='📝Добавить вопрос',
                            callback_data='add_question')

ib_2 = InlineKeyboardButton(text='⬅️Назад',
                            callback_data='back')

ikb_admin_add_question = InlineKeyboardMarkup()

ikb_admin_add_question.add(ib_1)
ikb_admin_add_question.add(ib_2)
