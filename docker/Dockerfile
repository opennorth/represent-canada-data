FROM ubuntu:18.04

# Base setup
RUN apt-get -y update
# Needed by add-apt-repository
RUN apt-get -y install software-properties-common
# Needed by ogrinfo
RUN add-apt-repository -y ppa:ubuntugis/ppa
# Python
RUN apt-get -y install python3 python3-pip python3-dev build-essential python3-invoke python3-lxml python3-unidecode python3-regex libxml2-dev libxslt-dev lib32z1-dev git sudo
# Others
RUN apt-get -y install npm curl unzip gdal-bin
RUN apt-get clean

# Python packages (might not need virtualenv)
RUN pip3 install virtualenv virtualenvwrapper ndg_httpsclient tidy flake8

# .bashrc
RUN echo 'export WORKON_HOME=$HOME/.virtualenvs' >> $HOME/.bashrc
RUN echo 'export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6' >> $HOME/.bashrc
RUN echo 'export PROJECT_HOME=/src/represent' >> $HOME/.bashrc
RUN echo 'source /usr/local/bin/virtualenvwrapper.sh' >> $HOME/.bashrc

RUN mkdir /src

WORKDIR /src/represent
