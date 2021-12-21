from datetime import timedelta
from decimal import Decimal
from typing import Optional, Dict, Any

from pydantic import BaseModel

class OrderPostPydantic(BaseModel):
    shop_id: int
    product_id: int
    count: int
    first_name: str
    surname: str
    patronymic: str
    phone_number: str
    order_confirmation: bool


class ProductPostPydantic(BaseModel):
    name: str
    firm: str
    model: str
    tech_params: Dict[str, Any]
    price: Decimal
    warranty_period: timedelta
    shop_id: Optional[int]


class ShopPostPydantic(BaseModel):
    email: str
    delivery_payment: bool
