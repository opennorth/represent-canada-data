FROM ubuntu:18.04

# Base setup
# Need this for add-apt-repository
RUN apt-get -y update \
  && apt-get -y install software-properties-common

# Need this for ogrinfo
RUN add-apt-repository -y ppa:ubuntugis/ppa

# Python and other goodies
RUN apt-get -y install python3 python3-pip python3-dev build-essential python3-invoke python3-lxml python3-unidecode python3-regex libxml2-dev libxslt-dev lib32z1-dev git sudo npm curl unzip gdal-bin \
  && apt-get clean

# Python packages (don't think we need virtualenv stuff bit just in case)
RUN pip3 install virtualenv virtualenvwrapper ndg_httpsclient tidy flake8

# .bashrc
RUN echo 'export WORKON_HOME=$HOME/.virtualenvs' >> $HOME/.bashrc
RUN echo 'export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6' >> $HOME/.bashrc
RUN echo 'export PROJECT_HOME=/src/represent' >> $HOME/.bashrc
RUN echo 'source /usr/local/bin/virtualenvwrapper.sh' >> $HOME/.bashrc

RUN mkdir /src

WORKDIR /src/represent
