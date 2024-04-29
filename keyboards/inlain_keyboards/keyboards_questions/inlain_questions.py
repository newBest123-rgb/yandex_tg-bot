from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


questions_kb = InlineKeyboardMarkup()

one_questions_ib = InlineKeyboardButton(text='Первый вопрос',
                                        callback_data='first_questions')

two_questions_ib = InlineKeyboardButton(text='Второй вопрос',
                                        callback_data='second_questions')

three_questions_ib = InlineKeyboardButton(text='Третий вопрос',
                                          callback_data='third_questions')

four_questions_ib = InlineKeyboardButton(text='Четвёртый вопрос',
                                         callback_data='fourth_questions')

five_questions_ib = InlineKeyboardButton(text='Пятый вопрос',
                                         callback_data='fiveth_questions')

six_questions_ib = InlineKeyboardButton(text='Шестой вопрос',
                                        callback_data='sixth_questions')

seven_questions_ib = InlineKeyboardButton(text='Седьмой вопрос',
                                          callback_data='seventh_questions')

ib_back = InlineKeyboardButton(text='⬅️Назад',
                               callback_data='back')

questions_kb.add(one_questions_ib)
questions_kb.add(two_questions_ib)
questions_kb.add(three_questions_ib)
questions_kb.add(four_questions_ib)
questions_kb.add(five_questions_ib)
questions_kb.add(six_questions_ib)
questions_kb.add(seven_questions_ib)
questions_kb.add(ib_back)
