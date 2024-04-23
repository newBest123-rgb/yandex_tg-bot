from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config.api_token import URL_GUIDE

ib_back_and_guide = InlineKeyboardButton(text='⬅️Назад',
                                         callback_data='back')

ib_back_and_guide_link = InlineKeyboardButton(text='👩🏻‍🎓Всё руководство',
                                              callback_data='link',
                                              url=URL_GUIDE)

kb_back_and_guide = InlineKeyboardMarkup()

kb_back_and_guide.add(ib_back_and_guide_link)
kb_back_and_guide.add(ib_back_and_guide)
