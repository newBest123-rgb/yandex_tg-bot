from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from data_base.db_users.db_users import recording_users
from data_base.db_add_users.db_add_users import id_users_admin
from data_base.db_show_users.db_show_users import show_users

from keyboards.inlain_keyboards.keyboards_menu.inlain_menu import ikb
from keyboards.inlain_keyboards.keyboards_back.inlain_back_questions import kb_back
from keyboards.inlain_keyboards.inlain_keyboards_admin.inlain_keyboards_admin_menu import ikb_admin

from keyboards.reply_keyboards.keyboards_menu.reply_menu import kb_reply_menu

from config.api_token import TOKEN
from config.api_token import PARSE_MODE_HTML
from config.api_token import ADMIN_ID
from config.api_token import SIGN_UP_ADMIN

from text.text_commands_bot.text_command_start import START_TEXT
from text.text_commands_bot.text_command_description import DESCRIPTION_TEXT
from text.text_commands_bot.text_command_contacts import TEXT_COMMAND_CONTACTS

from functions.commands.help_command import HELP_COMMAND
from functions.on_startup.on_startup import on_startup

from functions.callback.other.callback_aplication import callback_query_aplication
from functions.callback.other.callback_paid_services import callback_query_paid_services
from functions.callback.other.callback_contacts_rigestr import callback_query_contacts_rigestr
from functions.callback.questions.callback_questions import callback_query_questions
from functions.callback.questions.callback_first_questions import callback_query_first_questions
from functions.callback.questions.callback_second_questions import callback_query_second_questions
from functions.callback.questions.callback_third_questions import callback_query_third_questions
from functions.callback.questions.callback_fourth_questions import callback_query_fourth_questions
from functions.callback.questions.callback_fiveth_questions import callback_query_fiveth_questions
from functions.callback.questions.callback_sixth_questions import callback_query_sixth_questions
from functions.callback.questions.callback_seventh_questions import callback_query_seventh_questions
from functions.callback.about_us.callback_about_us import callback_contacts_hospital
from functions.callback.about_us.callback_about_us_contacts import callback_about_us_contacts
from functions.callback.about_us.callback_about_us_guide import callback_about_us_guide
from functions.callback.about_us.callback_about_us_home import callback_about_us_home
from functions.callback.back.callback_back import callback_back_query_questions
from functions.callback.admin.callback_admin_menu import callback_admin_menu
from functions.callback.admin.callback_admin_panel_users import callback_admin_menu_back
from functions.callback.admin.callback_admin_panel_user_id import callback_admin_users_id

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_start_bot(message: types.Message):
    if message.from_user.id == int(ADMIN_ID):
        await message.answer(text=SIGN_UP_ADMIN,
                             reply_markup=ikb_admin)
    else:
        await bot.send_message(chat_id=message.from_user.id,
                               text=START_TEXT,
                               reply_markup=ikb,
                               parse_mode=PARSE_MODE_HTML)

    await recording_users(message)


@dp.message_handler(commands=['menu'])
async def start_menu_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=START_TEXT,
                           reply_markup=ikb,
                           parse_mode=PARSE_MODE_HTML)
    await message.delete()


@dp.message_handler(Text('Показать меню'))
async def pokaz_menu_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=START_TEXT,
                           reply_markup=ikb,
                           parse_mode=PARSE_MODE_HTML)
    await message.delete()


@dp.message_handler(Text('Пользователи'))
async def users_bot(message: types.Message):
    await show_users(message)


@dp.message_handler(Text('Кто подал заявку'))
async def users_bot(message: types.Message):
    await id_users_admin(message)


@dp.callback_query_handler()
async def callback_query(callback: types.CallbackQuery):
    await callback_query_paid_services(callback)
    await callback_query_aplication(callback)
    await callback_query_contacts_rigestr(callback)
    await callback_query_questions(callback)
    await callback_query_first_questions(callback)
    await callback_query_second_questions(callback)
    await callback_query_third_questions(callback)
    await callback_query_fourth_questions(callback)
    await callback_query_fiveth_questions(callback)
    await callback_query_sixth_questions(callback)
    await callback_query_seventh_questions(callback)
    await callback_back_query_questions(callback)
    await callback_contacts_hospital(callback)
    await callback_about_us_contacts(callback)
    await callback_about_us_guide(callback)
    await callback_about_us_home(callback)
    await callback_admin_menu(callback)
    await callback_admin_menu_back(callback)
    await callback_admin_users_id(callback)


@dp.message_handler(commands=['help'])
async def help_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=HELP_COMMAND,
                           reply_markup=kb_reply_menu,
                           parse_mode=PARSE_MODE_HTML)
    await message.delete()


@dp.message_handler(commands=['description'])
async def description_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=DESCRIPTION_TEXT,
                           reply_markup=kb_back,
                           parse_mode=PARSE_MODE_HTML)
    await message.delete()


@dp.message_handler(commands=['contacts'])
async def contacts_bot(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=TEXT_COMMAND_CONTACTS,
                           reply_markup=kb_back,
                           parse_mode=PARSE_MODE_HTML)
    await message.delete()


@dp.message_handler(commands=['id'])
async def id_bot(message: types.Message):
    await message.answer(text=f'{message.from_user.id}',
                         reply_markup=kb_back,
                         parse_mode=PARSE_MODE_HTML)
    await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
