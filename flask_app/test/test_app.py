from factory import create_app

app = create_app('test')
client = app.test_client()

assert app.config['SQL_ADDRESS'] in client.get('/').data.decode('utf8')
