# handlers/add_game.py

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import StateFilter

router = Router()

@router.callback_query(F.data.startswith("select_game:"))
async def on_game_selected(callback: CallbackQuery):
    game_id = int(callback.data.split(":")[1])

    # твоя логика сохранения
    await callback.message.edit_text(f"✅ Игра #{game_id} добавлена в список!")
    await callback.answer()  # убирает "часики" на кнопке

@router.callback_query(F.data == "cancel")
async def on_cancel(callback: CallbackQuery):
    await callback.message.edit_text("Отменено.")
    await callback.answer()