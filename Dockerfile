# Build:
# docker build --tag="${PWD##*/}" .
#
# Run tests:
# docker run --user ${UID}:${GROUPS} --rm --tty --interactive --volume "${PWD}":/var/task "${PWD##*/}"


FROM ubuntu:16.04


LABEL maintainer="django-thummer"


# Install required os packages
RUN apt-get update --quiet --yes
RUN apt-get install --quiet --yes avahi-daemon dictionaries-common language-pack-en
RUN apt-get install --quiet --yes apt-transport-https build-essential byobu ca-certificates gettext git graphicsmagick imagemagick libboost-python-dev libffi-dev libgdal1-dev libgeos-dev libgraphicsmagick++-dev libjpeg-dev libmagickwand-dev libmemcached-dev libssl-dev libpng-dev libpq-dev libproj-dev libspatialite-dev libsqlite3-dev libsqlite3-mod-spatialite libxslt1-dev libyaml-dev lynx python3-dev python3-venv wget zlib1g-dev
RUN apt-get install --quiet --yes firefox


# Install required python packages
ADD . /var/task
RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/python -m pip install --force --upgrade pip
RUN /opt/venv/bin/python -m pip install --force --upgrade setuptools urllib3[secure]
RUN /opt/venv/bin/python -m pip install /var/task[tests]

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
RUN tar -xvf geckodriver-*.tar.gz --directory /usr/local/bin/


# Configure environment
ENV HOME /tmp
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONWARNINGS d


# Entrypoint
WORKDIR /var/task
USER 1000:1000
ENTRYPOINT ["/opt/venv/bin/python", "setup.py"]
CMD ["test"]
