from aiosales.models import Product


class ProductsService:

    def __init__(self, product_repo, shop_repo):
        self.product_repo = product_repo
        self.shop_repo = shop_repo

    async def get_by_id(self, _id: int):
        return await self.product_repo.get(id=id)

    async def get_with_metrics(self):
        return await self.product_repo.filter_with_done_delivery()

    async def create_product(self, product_data, shop_id):
        product = Product(**product_data)
        await self.product_repo.add(product)
        if shop_id:
            shop = await self.shop_repo.get(id=shop_id)
            await product.shops.add(shop)
