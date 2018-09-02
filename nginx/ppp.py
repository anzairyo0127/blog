from orator import DatabaseManager, Model

config = {
    'mysql': {
    'driver': 'mysql',
    'host': '192.168.99.100',
    'database': 'db_blog',
    'user': 'root',
    'password': 'root',
    'charset': 'utf8',
    'prefix': ''
    }
}


db = DatabaseManager(config)

Model.set_connection_resolver(db)


class Blog(Model):
    __table__ = 'blog'


blog = Blog()
print(blog.find(1).honbun)