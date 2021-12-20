from tortoise import fields
from tortoise import Model


class Shop(Model):
    id: fields.IntField
    email: fields.CharField
    delivery_payment: fields.BooleanField

    products: fields.ManyToManyRelation['Shop']
    orders: fields.ReverseRelation['Order']


class Product(Model):
    id: fields.IntField
    name: fields.CharField
    firm: fields.CharField
    model: fields.CharField
    tech_params: fields.JSONField
    price: fields.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    warranty_period: fields.TimeDeltaField
    image: fields.BinaryField

    shops: fields.ManyToManyRelation[Shop]
    orders: fields.ReverseRelation['Order']


class Order(Model):
    id: fields.IntField
    date: fields.DatetimeField
    count: fields.IntField
    first_name: fields.CharField
    surname: fields.CharField
    patronymic: fields.CharField
    phone_number: fields.CharField
    order_confirmation: fields.BooleanField

    shop: fields.ForeignKeyRelation[Shop]
    product: fields.ForeignKeyRelation[Product]
    delivery: fields.ReverseRelation['Delivery']

    def client_full_name(self) -> str: ...


class Delivery(Model):
    id: fields.IntField
    date: fields.DatetimeField
    address: fields.CharField
    client_first_name: fields.CharField
    client_surname: fields.CharField
    client_patronymic: fields.CharField
    courier_first_name: fields.CharField
    courier_surname: fields.CharField
    courier_patronymic: fields.CharField

    order: fields.OneToOneRelation[Order]

    def client_full_name(self) -> str: ... 

    def courier_full_name(self) -> str: ...
