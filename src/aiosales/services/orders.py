from tortoise.expressions import Q

from aiosales.models import Order


class OrdersService:

    def __init__(self, shop_repo, product_repo, order_repo):
        self.shop_repo = shop_repo
        self.product_repo = product_repo
        self.order_repo = order_repo

    async def create_order(self, order_data, shop_id, product_id):
        shop = await self.shop_repo.get(id=shop_id)
        product = await self.product_repo.get(id=product_id)
        order = Order(
            **order_data,
            shop=shop,
            product=product
        )
        await self.order_repo.add(order)

    async def filter_orders(self, shops, products, **attributes):
        filter_set = Q(**attributes)
        if shops:
            filter_set &= Q(shop_id__in=shops)
        if products:
            filter_set &= Q(product_id__in=products)
        return await self.order_repo.filter(filter_set)
