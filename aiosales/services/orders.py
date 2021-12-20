from aiosales.models import Order


class OrdersService:

    def __init__(self, shop_repo, product_repo, order_repo):
        self.shop_repo = shop_repo
        self.product_repo = product_repo
        self.order_repo = order_repo

    async def create_order(self, order_data):
        shop_id = order_data.pop('shop_id')
        product_id = order_data.pop('product_id')
        shop = await self.shop_repo.get(reference=shop_id)
        product = await self.product_repo.get(reference=product_id)
        __import__('pdb').set_trace()
        order = Order(
            **order_data,
            shop_id=shop_id,
            product_id=product_id
        )
        await self.order_repo.add(order)
