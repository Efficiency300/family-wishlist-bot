from db.database import Base
from sqlalchemy.orm import Mapped , mapped_column

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(nullable=False)
    
    
class WhishlistItem(Base):
    __tablename__ = "wishlist_items"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(nullable=False)
    game_name: Mapped[str] = mapped_column(nullable=False)
    game_url: Mapped[str] = mapped_column(nullable=False)
    current_price: Mapped[float] = mapped_column(nullable=False)
    lowest_price: Mapped[float] = mapped_column(nullable=False)
    
