from tortoise import Tortoise


async def init_database(db_url: str):
    await Tortoise.init(
        db_url=db_url,
        modules={
            'models': [
                'models'
            ]
        }
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()
