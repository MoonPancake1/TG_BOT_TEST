from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from create_bot import admins

def main_kb(user_telegram_id: int):
    kb_list = [[
                    KeyboardButton(text="📖 О нас"), 
                    KeyboardButton(text="🧟 Профиль")
                ],
                [
                    KeyboardButton(text="⚙️ Настройки"),
                    KeyboardButton(text="📚 Каталог")
                ]]
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    
    return keyboard


def create_spec_kb():
    kb_list = [
        [
            KeyboardButton(text="Геопозиция", 
                           request_location=True)
        ],
        [
            KeyboardButton(text="Номер телефона",
                           request_contact=True)
        ]
    ]
    
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Воспользуйтесь меню:"
    )
    
    return keyboard
