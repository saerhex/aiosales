from tortoise import Tortoise


class Database:

    def __init__(self, db_url):
        self.__db_url = db_url

    async def init_database(self):
        await Tortoise.init(
            db_url=self.__db_url,
            modules={
                'models': [
                    'models'
                ]
            }
        )
        await Tortoise.generate_schemas()
        yield
        await Tortoise.close_connections()
