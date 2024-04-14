from aiogram.fsm.state import StatesGroup, State

class StateAddPost(StatesGroup):
    GET_CHANNEL = State()
    GET_POST = State()
    GET_COMPLITING= State()
    FINISH = State()
    CLEAR = State()