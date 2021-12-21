from aiosales.repositories.shop import ShopRepository


class ShopService:
    shop_repo: ShopRepository
    def __init__(self, shop_repo: ShopRepository) -> None: ...
    async def create_shop(self, shop_data) -> None: ...
