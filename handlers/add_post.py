from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.channel_selection import channel_selection_kb
from keyboards.add_post_menu import add_post_menu_kb, delete_kb, finish_add_post_kb
from states.add_post import StateAddPost
from database.requests import get_channel

rt = Router()

@rt.callback_query(F.data == "to_create_post")
async def channel_selection(cl: CallbackQuery, state: FSMContext):
    await cl.message.edit_text("Выбирете канал для публикации:",
                               reply_markup=await channel_selection_kb())
    await state.set_state(StateAddPost.GET_CHANNEL)
    await cl.answer("")

@rt.callback_query(F.data.startswith("to_post_in_"), StateAddPost.GET_CHANNEL)
async def create_post(cl: CallbackQuery, state: FSMContext, bot: Bot):
    id = cl.data.split("_")[3]
    channel = await get_channel(id)
    await state.update_data(tg_channel_id=channel.tg_id)
    await cl.message.edit_text(f"Вы выбрали канал <b>«{channel.title}»</b> для постинга.")
    await bot.send_message(chat_id=cl.from_user.id,
                           text=(f"Отправьте боту то, что хотите опубликовать. "
                                f"Это может быть всё, что угодно – текст, фото, видео, даже стикеры."),
                           reply_markup=add_post_menu_kb)
    await state.set_state(StateAddPost.GET_POST)
    await cl.answer("")

@rt.message(StateAddPost.GET_POST, F.text, F.text != "Далее", F.text != "Отмена") #обработка для текста
async def get_post(m: Message, state: FSMContext):
    await state.update_data(post_text=m.text)
    await m.answer("Предпросмотр поста:")
    await m.answer(f"{m.text}")
    await state.set_state(StateAddPost.GET_COMPLITING)

@rt.message(F.text == "Далее", StateAddPost.GET_COMPLITING)
async def completing_addition(m: Message, state: FSMContext, bot: Bot):
    await m.answer(text=f"Сообщение готово к отправке!", reply_markup=delete_kb)
    await m.answer(f"Вы хотите опубликовать пост прямо сейчас или отложить? ", reply_markup=finish_add_post_kb)
    await state.set_state(StateAddPost.FINISH)
@rt.message(F.text == "Далее")
async def completing_addition(m: Message, state: FSMContext):
    await m.answer("Вы еще ничего не ввели!")

@rt.callback_query(F.data == "to_publish_post", StateAddPost.FINISH)
async def publish_post(cl: CallbackQuery, state: FSMContext, bot: Bot):
    post = await state.get_data()
    channel_id = post["tg_channel_id"]
    post_text = post["post_text"]
    await bot.send_message(chat_id=channel_id, text=post_text)
    await state.set_state(StateAddPost.CLEAR)
    await cl.message.edit_text("Пост успешно опубликован!")
    await cl.answer("")

@rt.message(StateAddPost.CLEAR)
async def add_post_clear_state(m: Message, state: FSMContext):
    await state.clear()







