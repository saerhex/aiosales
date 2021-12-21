

class ProductsService:

    def __init__(self, product_repo):
        self.product_repo = product_repo

    async def get_by_id(self, _id: int):
        return await self.product_repo.get(id=id)

    async def get_with_metrics(self):
        return await self.product_repo.filter_with_done_delivery()
