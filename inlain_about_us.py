from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

about_us_kb = InlineKeyboardMarkup()

about_us_button_contacts = InlineKeyboardButton(text='☎️Контакты',
                                                callback_data='about_us_contacts')

about_us_button_guide = InlineKeyboardButton(text='💁🏻‍♀️Руководство',
                                             callback_data='about_us_guide')

about_us_button_hospital = InlineKeyboardButton(text='🗺️Как до нас добраться',
                                                callback_data='about_us_home')

about_us_button_back = InlineKeyboardButton(text='⬅️Назад',
                                            callback_data='back')

about_us_kb.add(about_us_button_contacts, about_us_button_guide)
about_us_kb.add(about_us_button_hospital)
about_us_kb.add(about_us_button_back)
