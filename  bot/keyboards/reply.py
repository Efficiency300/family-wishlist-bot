# keyboards/reply.py

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="📋 Мой список"),
        KeyboardButton(text="👨‍👩‍👧 Список семьи"),
    )
    builder.row(
        KeyboardButton(text="➕ Добавить игру"),
        KeyboardButton(text="📄 Документ"),
    )

    return builder.as_markup(resize_keyboard=True)