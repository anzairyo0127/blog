FROM ubuntu:18.04

ARG python_Ver="3.6.5"
ARG pyenvpath="/.pyenv"
ARG flask_Ver="1.0.2"
ARG name_of_venv="appflask"
ARG uWSGI_Ver="2.0.17"
# MySQL-ClientのVer指定
ARG mysql_mj_ver="5"
ARG mysql_mi_ver="7"
ARG mysql_mn_ver="22"
ARG pymysql_Ver="0.9.2"
ARG orator_Ver="0.9.7"

# pyenv PATH environment variable
ENV PYENV_ROOT ${pyenvpath}
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# network test tools
RUN apt update -y && apt install -y iputils-ping net-tools curl wget nmap

# pyenv
RUN apt install -y \
make build-essential libssl-dev zlib1g-dev libbz2-dev git \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils
RUN git clone git://github.com/yyuu/pyenv.git ${pyenvpath}
RUN pyenv install ${python_Ver}
RUN pyenv local ${python_Ver}

# flask and virtualenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ${pyenvpath}/plugins/pyenv-virtualenv
RUN pyenv virtualenv ${version} ${name_of_venv}
RUN pyenv local ${name_of_venv}
RUN pip install -U pip
RUN pip install Flask==${flask_Ver}

# uWSGI
RUN pip install uwsgi==${uWSGI_Ver}

# orator (&mysql-client pymysql)
RUN apt install -y mysql-client-${mysql_mj_ver}.${mysql_mi_ver}=${mysql_mj_ver}.${mysql_mi_ver}.${mysql_mn_ver}-0ubuntu18.04.1
RUN pip install pymysql==${pymysql_Ver}
RUN pip install orator==${orator_Ver}