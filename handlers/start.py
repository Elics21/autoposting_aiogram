from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

import database.requests as rq
from keyboards.start import start_kb

rt = Router()

@rt.message(CommandStart())
async def command_start(m: Message):
    await rq.set_user(m.from_user.id, m.from_user.username)
    await m.answer("Здесь вы можете создавать посты, просматривать статистику и выполнять другие задачи.",
                   reply_markup=start_kb)
