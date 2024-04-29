from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config.api_token import URL_HOSPITAL


ib1 = InlineKeyboardButton(text='📝Подать заявку',
                           callback_data='application')


ib2 = InlineKeyboardButton(text='❓Частые вопросы',
                           callback_data='chast_vopros')

ib3 = InlineKeyboardButton(text='💳Платные услуги',
                           callback_data='paid_services')


ib5 = InlineKeyboardButton(text='🏥Ближайшие больницы',
                           callback_data='hospital',
                           url=URL_HOSPITAL)


ib8 = InlineKeyboardButton(text='🏛️О нас',
                           callback_data='about_us')

ikb = InlineKeyboardMarkup()

ikb.add(ib1)
ikb.add(ib2, ib3)
ikb.add(ib5, ib8)
