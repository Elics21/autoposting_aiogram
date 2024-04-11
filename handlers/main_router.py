from aiogram import Router
from handlers.start import rt as start_rt
from handlers.add_channel import  rt as add_channel_rt

main_router = Router()

main_router.include_routers(
    start_rt,
    add_channel_rt
)