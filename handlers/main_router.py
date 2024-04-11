from aiogram import Router
from handlers.start import rt as start_rt

main_router = Router()

main_router.include_routers(
    start_rt,

)