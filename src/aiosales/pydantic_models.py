from datetime import timedelta
from decimal import Decimal
from typing import Dict, Any, Optional

from pydantic import BaseModel
from pydantic import Field


class OrderPostPydantic(BaseModel):
    shop_id: int
    product_id: int
    count: int = Field(..., gt=0)
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
    price: Decimal = Field(..., gt=0)
    warranty_period: timedelta
    shop_id: Optional[int]


class ShopPostPydantic(BaseModel):
    email: str = Field(..., regex=r'.+@.+\..+')
    delivery_payment: bool
