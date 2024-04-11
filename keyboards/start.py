from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Создать пост", callback_data="to_create_post")],
    [InlineKeyboardButton(text="Добавить канал", callback_data="to_add_channel")]
])