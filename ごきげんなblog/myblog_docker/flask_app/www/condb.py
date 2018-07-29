from orator import DatabaseManager, Model
from orator import Schema

config = { 
    'mysql': {
    'driver': 'mysql',
    'host': 'mysql_ctr',
    'database': 'db',
    'user': 'lion',
    'password': 'lion',
    'prefix': ''
    }
}

db = DatabaseManager(config)

schema = Schema(db)

with schema.create('users') as table:
    table.increments('id')
    table.string('user').nullable()
    table.string('email')
    table.datetime('created_at')
    table.datetime('updated_at')
