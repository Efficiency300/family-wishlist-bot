from pathlib import Path
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, Message
from bot.keyboards.reply import main_menu_kb

router = Router()

WELCOME_PHOTO = FSInputFile(Path(__file__).parent.parent / "assets" / "welcome.jpg")
WELCOME_TEXT = (
    "Hello! I'm a family wishlist bot. I can help you to create and manage "
    "your family wishlist. Just send me a message and I'll do my best to help you!"
)


@router.message(CommandStart())
async def start_command_handler(message: Message) -> None:
    """
    Handler for the /start command, which will be called when user starts the bot
    """
    await message.answer_photo(photo=WELCOME_PHOTO, caption=WELCOME_TEXT, reply_markup=main_menu_kb())