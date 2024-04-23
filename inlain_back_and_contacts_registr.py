from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ib1 = InlineKeyboardButton(text='☎️Контакты',
                           callback_data='contacts_rigestr')

ib2 = InlineKeyboardButton(text='⬅️Назад',
                           callback_data='back')

inline_con_rigestr_kb = InlineKeyboardMarkup(row_width=2)

inline_con_rigestr_kb.add(ib1, ib2)
