from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

add_post_menu_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Отменить"), KeyboardButton(text="Далее")]
], resize_keyboard=True)

finish_add_post_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Опубликовать", callback_data="to_publish_post"),
     InlineKeyboardButton(text="Отложить", callback_data="to_set_delay_post")],
    [InlineKeyboardButton(text="« Назад", callback_data="to_back_adding_post")]
])

delete_kb = ReplyKeyboardRemove(remove_keyboard=True)