FROM python:3.6

ARG flask_Ver="1.0.2"
ARG uWSGI_Ver="2.0.17"
ARG pip_mysqlclient="1.3.13"
ARG pymysql_Ver="0.9.2"
ARG orator_Ver="0.9.7"

## mysql-client
RUN apt update -y && apt install mysql-client -y

## flask and virtualenv
RUN pip install Flask==${flask_Ver}

# uWSGI
RUN pip install uwsgi==${uWSGI_Ver}

# orator (&pymysql)
RUN pip install pymysql==${pymysql_Ver}
RUN pip install mysqlclient==${pip_mysqlclient}
RUN pip install orator==${orator_Ver}