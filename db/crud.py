from db.database import async_session
from db.models import User, WhishlistItem
from sqlalchemy import select, delete, func

class CRUD:
    @staticmethod
    async def add_user(telegram_id: int, username: str) -> None:
        async with async_session() as session:
            async with session.begin():
                session.add(User(telegram_id=telegram_id, username=username))

                
    @staticmethod
    async def delete_game_from_wishlist(user_id: int, game_name: str) -> None:
        async with async_session() as session:
            async with session.begin():
                await session.execute(
                    delete(WhishlistItem).where(
                        WhishlistItem.user_id == user_id,
                        WhishlistItem.game_name == game_name
                    )
                )
                
                
                
                
    @staticmethod
    async def get_list_of_all_games(page: int = 1 , size: int = 20):
        offset = (page - 1) * size
        async with async_session() as session:
            total = await session.scalar(select(func.count())).select_from(WhishlistItem)
            result = await session.execute(
                select(WhishlistItem).order_by(WhishlistItem.id).offset(offset).limit(size))
            items  = result.scalars().all()
            
        total_pages = (total + size - 1) // size if total else 0
        return {
            "items": items,
            "total": total,
            "page": page,
            "size": size,
            "total_pages": total_pages,
        }
        
    @staticmethod
    async def add_game_to_wishlist(user_id: int, game_name: str, game_url: str, current_price: float, lowest_price: float) -> None:
        async with async_session() as session:
            async with session.begin():
                session.add(WhishlistItem(
                    user_id=user_id,
                    game_name=game_name,
                    game_url=game_url,
                    current_price=current_price,
                    lowest_price=lowest_price
                ))
                
    @staticmethod
    async def get_wishlist_by_user_id(user_id: int) -> list[WhishlistItem]:
        async with async_session() as session:
            result = await session.execute(
                select(WhishlistItem).where(WhishlistItem.user_id == user_id)
            )
            return result.scalars().all()