FROM python:3.6

ARG flask_Ver="1.0.2"
ARG uWSGI_Ver="2.0.17"
ARG pymysql_Ver="0.9.2"
ARG flask_sqlachemy_Ver="2.3.2"
ARG flask_migrate_Ver="2.2.1"

## flask and virtualenv
RUN pip install Flask==${flask_Ver}

# uWSGI
RUN pip install uwsgi==${uWSGI_Ver}

# orator (&pymysql)
RUN pip install pymysql==${pymysql_Ver}
RUN pip install Flask-SQLAlchemy==${flask_sqlachemy_Ver}
RUN pip install Flask-Migrate==${flask_migrate_Ver}