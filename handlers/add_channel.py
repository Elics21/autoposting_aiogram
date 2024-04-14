from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, ChatMemberAdministrator
from aiogram.fsm.context import FSMContext

from keyboards.start import start_kb
from states.add_channel import StateAddChannel
import database.requests as rq

rt = Router()

@rt.callback_query(F.data == "to_add_channel")
async def add_channel(cl: CallbackQuery, state: FSMContext):
    await cl.message.edit_text("Перешлите мне любое сообщение из канала, который хотите привязать")
    await state.set_state(StateAddChannel.GET_CHANNEL)
    await cl.answer("")


@rt.message(F.forward_from_chat, StateAddChannel.GET_CHANNEL)
async def forward_channel_post(m: Message, bot: Bot, state: FSMContext):
    chat_id = m.forward_from_chat.id
    bot_status = await bot.get_chat_member(chat_id=chat_id, user_id=bot.id)
    if bot_status.can_post_messages == True:
        channel_name = m.forward_from_chat.title
        await rq.set_channel(chat_id, channel_name)
        await m.answer(f"Канал '{channel_name} успешно добавлен!'", reply_markup=start_kb)
        await state.clear()
    else:
        await m.answer('Дайте боту права на "Публикация постов" и еще раз перешлите сообщение!')

@rt.message(StateAddChannel.GET_CHANNEL)
async def error_add(m: Message):
    await m.answer("Произошла ошибка, перешлите сообщение еще раз!")
