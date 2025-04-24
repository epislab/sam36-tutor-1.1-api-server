from com.epislab.utils.creational.singleton import db_singleton


class QueryBuilder:
    def __init__(self):
        self.db = None
        self.query_text = ""
        self.params = []

    def connect(self):
        if not self.db:
            self.db = db_singleton
        return self

    def query(self, sql: str):
        self.query_text = sql
        return self

    def params(self, *args):
        self.params = args
        return self

    async def execute(self):
        if not self.db:
            raise ValueError("Database connection is not established.")
        
        async with self.db.pool.acquire() as connection:
            return await connection.fetch(self.query_text, *self.params)