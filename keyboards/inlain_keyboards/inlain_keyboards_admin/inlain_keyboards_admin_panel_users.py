from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ib_1 = InlineKeyboardButton(text='📝Показать ID всех пользователей',
                            callback_data='show_users')

ib_2 = InlineKeyboardButton(text='⬆️Вернуться в меню',
                            callback_data='back_in_menu')

ikb_admin_show_users = InlineKeyboardMarkup()

ikb_admin_show_users.add(ib_1)
ikb_admin_show_users.add(ib_2)
