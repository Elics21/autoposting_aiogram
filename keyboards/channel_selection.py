from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from database.requests import get_all_channel


async def channel_selection_kb():
    keyboard = InlineKeyboardBuilder()
    all_channel = await get_all_channel()
    for channel in all_channel:
        keyboard.add(InlineKeyboardButton(text=f"{channel.title}", callback_data=f"to_post_in_{channel.id}"))
    return keyboard.adjust(1).as_markup()