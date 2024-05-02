from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from data_base.db_add_users.db_add_users import id_users_admin
from data_base.db_show_users.db_show_users import show_users

from config.api_token import TOKEN

from functions.on_startup.on_startup import on_startup

from functions.commands.main_commands.contacts_commands import func_contacts_bot
from functions.commands.main_commands.description_commands import func_description_bot
from functions.commands.main_commands.help_commands import func_help_bot
from functions.commands.menu_commands.pokaz_menu_commands import func_pokaz_menu_bot
from functions.commands.menu_commands.menu_commands import func_start_menu_bot
from functions.commands.start_commands.start_comands import func_start_start_bot

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
    await func_start_start_bot(message)


@dp.message_handler(commands=['menu', 'Menu', 'MENU'])
async def start_menu_bot(message: types.Message):
    await func_start_menu_bot(message)


@dp.message_handler(Text('Показать меню'))
async def pokaz_menu_bot(message: types.Message):
    await func_pokaz_menu_bot(message)


@dp.message_handler(Text('Пользователи'))
async def add_users_bot(message: types.Message):
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


@dp.message_handler(commands=['help', 'Help', 'HELP'])
async def help_bot(message: types.Message):
    await func_help_bot(message)


@dp.message_handler(commands=['description', 'Description', 'DESCRIPTION'])
async def description_bot(message: types.Message):
    await func_description_bot(message)


@dp.message_handler(commands=['contacts', 'Contacts', 'CONTACTS'])
async def contacts_bot(message: types.Message):
    await func_contacts_bot(message)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
