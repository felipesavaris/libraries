import os


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")


config_database = Config()
print('url database --->', config_database.DATABASE_URL)