from flask import Flask, render_template, request, url_for
from orator import DatabaseManager, Model

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

Model.set_connection_resolver(db)

class Users(Model):
    __table__ = 'users'


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # from処理
        userDitail = request.form
        name = userDitail['name']
        email = userDitail['email']
        # DB処理
        users = Users()
        users.user = name
        users.email = email
        users.save()
        return 'SUCCESS！'
    return render_template('index.html')

@app.route('/users')
def users():
    # DB処理items = Item.all()
    users = Users.all()
    return render_template('users.html',
    users=users,
    )

if __name__ == "__main__":
    app.run(debug=True)