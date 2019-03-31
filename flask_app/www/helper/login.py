from flask_login import UserMixin

from objects.logins import login
# Our mock database.
users = {'metarion@email.com': {'password': 'secret'}}


class User(UserMixin):
    pass


@login.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']

    return user
