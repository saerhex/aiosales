from aiosales.models import Shop


class ShopService:

    def __init__(self, shop_repo):
        self.shop_repo = shop_repo

    async def create_shop(self, shop_data):
        shop = Shop(**shop_data)
        await self.shop_repo.add(shop)
