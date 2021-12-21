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
