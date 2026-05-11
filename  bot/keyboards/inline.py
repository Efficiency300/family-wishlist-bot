# keyboards/inline.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def game_search_results_kb(
    games: list[dict],
    page: int = 0,
    page_size: int = 5
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    start = page * page_size
    page_games = games[start : start + page_size]

    for game in page_games:
        builder.row(
            InlineKeyboardButton(
                text=game["title"],
                callback_data=f"select_game:{game['id']}"
            )
        )

    # Навигация
    nav_buttons = []
    if page > 0:
        nav_buttons.append(
            InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page:{page - 1}")
        )
    if start + page_size < len(games):
        nav_buttons.append(
            InlineKeyboardButton(text="➡️ Вперёд", callback_data=f"page:{page + 1}")
        )
    if nav_buttons:
        builder.row(*nav_buttons)

    builder.row(
        InlineKeyboardButton(text="❌ Отмена", callback_data="cancel")
    )

    return builder.as_markup()