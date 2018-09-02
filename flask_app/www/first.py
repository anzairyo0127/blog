from orator import DatabaseManager, Model
from orator import Schema

config = {
    'mysql': {
    'driver': 'mysql',
    'host': '172.19.0.2',
    'database': 'db_blog',
    'user': 'lion',
    'password': 'lion',
    'prefix': ''
    }
}

db = DatabaseManager(config)

schema = Schema(db)

with schema.create('blog') as table:
    table.increments('id')
    table.string('title')
    table.string('honbun')
    table.datetime('created_at')
    table.datetime('updated_at')