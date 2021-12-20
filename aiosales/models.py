from tortoise import fields
from tortoise import Model


class Shop(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=64)
    delivery_payment = fields.BooleanField()

    products: fields.ManyToManyRelation['Shop']
    orders: fields.ReverseRelation['Order']


class Product(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    firm = fields.CharField(max_length=64)
    model = fields.CharField(max_length=64)
    tech_params = fields.JSONField()
    price = fields.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    warranty_period = fields.TimeDeltaField()
    image = fields.BinaryField(max_length=255)

    shops: fields.ManyToManyRelation[Shop] = fields.ManyToManyField(
        'models.Shop', related_name='products', on_delete=fields.CASCADE
    )
    orders: fields.ReverseRelation['Order']


class Order(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField(auto_now_add=True)
    count = fields.IntField()
    first_name = fields.CharField(max_length=32)
    surname = fields.CharField(max_length=32)
    patronymic = fields.CharField(max_length=32)
    phone_number = fields.CharField(max_length=32)
    order_confirmation = fields.BooleanField()

    shop: fields.ForeignKeyRelation[Shop] = fields.ForeignKeyField(
        'models.Shop', related_name='orders', on_delete=fields.RESTRICT
    )
    product: fields.ForeignKeyRelation[Product] = fields.ForeignKeyField(
        'models.Product', related_name='orders', on_delete=fields.RESTRICT
    )
    delivery: fields.ReverseRelation['Delivery']

    def client_full_name(self) -> str:
        return f'{self.surname} {self.first_name} {self.patronymic}'


class Delivery(Model):
    id = fields.IntField(pk=True)
    date = fields.DatetimeField(auto_now_add=True)
    address = fields.CharField(max_length=128)
    client_first_name = fields.CharField(max_length=32)
    client_surname = fields.CharField(max_length=32)
    client_patronymic = fields.CharField(max_length=32)
    courier_first_name = fields.CharField(max_length=32)
    courier_surname = fields.CharField(max_length=32)
    courier_patronymic = fields.CharField(max_length=32)

    order: fields.OneToOneRelation[Order] = fields.OneToOneField(
        'models.Order', related_name='delivery', on_delete=fields.RESTRICT
    )

    def client_full_name(self) -> str:
        return f'{self.client_surname} {self.client_first_name} {self.client_patronymic}'

    def courier_full_name(self) -> str:
        return f'{self.courier_surname} {self.courier_first_name} {self.courier_patronymic}'
