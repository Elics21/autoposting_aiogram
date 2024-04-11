from aiogram.fsm.state import StatesGroup, State

class StateAddChannel(StatesGroup):
    GET_CHANNEL = State()