from flaskr import db
from flaskr.models import Entry


db.create_all()
for i in range(1, 201):
    entry = Entry(
        title='title_:' + str(i),
        text='text_' + str(i),
        name='userID_' + str(i)
    )
    db.session.add(entry)

db.session.commit()

