from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

rt = Router()

@rt.message(CommandStart())
async def command_start(m: Message):
    await m.answer("Добро пожаловать!")