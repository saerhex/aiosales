from pydantic import BaseModel, Field


class OrderPydantic(BaseModel):
    shop_id: int
    product_id: int
    count: int = Field(..., gt=0)
    first_name: str
    surname: str
    patronymic: str
    phone_number: str
    order_confirmation: bool
