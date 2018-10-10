FROM                python:3.6.5-slim
MAINTAINER          rlaalsrbgk@gmail.com

# pip install uwsgi
RUN                 apt -y update && apt -y dist-upgrade
RUN                 apt -y install build-essential
RUN                 apt -y install nginx supervisor

COPY                ./requirements.txt  /srv/
RUN                 pip install --upgrade pip
RUN                 pip install -r /srv/requirements.txt

ENV                 BUILD_MODE              production
ENV                 DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY                ./requirements.txt  /srv/
RUN                 pip install -r /srv/requirements.txt

COPY                .   /srv/project

# Nginx
RUN                 cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf \
                            /etc/nginx/nginx.conf && \

                    cp -f   /srv/project/.config/${BUILD_MODE}/nginx_app.conf \
                            /etc/nginx/sites-available/ && \
                    rm -f   /etc/nginx/sites-enabled/* && \
                    ln -sf  /etc/nginx/sites-available/nginx_app.conf \
                            /etc/nginx/sites-enabled

# Supervisor config
RUN                 cp -f   /srv/project/.config/dev/supervisor_app.conf \
                            /etc/supervisor/conf.d/

# Run supervisor
CMD                 supervisord -n