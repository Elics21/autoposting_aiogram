from database.models import async_session
from database.models import User, Channel
from sqlalchemy import select

async def set_user(tg_id, user_name: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            user = User(tg_id=tg_id, user_name=user_name)
            session.add(user)
            await session.commit()

async def set_channel(tg_id, title: str):
    async with async_session() as session:
        channel = await  session.scalar(select(Channel).where(Channel.tg_id == tg_id))
        if not channel:
            channel = Channel(tg_id=tg_id, title=title)
            session.add(channel)
            await session.commit()

async def get_all_channel():
    async with async_session() as session:
        return await session.scalars(select(Channel))

async def get_channel(id: int):
    async with async_session() as session:
        return await session.scalar(select(Channel).where(Channel.id == id))