FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

ENV APP_NAME="RiotKit's services dashboard" \
    APP_ADMIN_TOKEN="YOUR-SECRET-ADMIN-KEY" \
    APP_PROVIDER="docker" \
    APP_PROVIDER_URL="unix:///var/run/docker.sock"

COPY ./uwsgi.ini /app/
COPY ./Makefile /app/
COPY ./setup.cfg /app/
COPY ./Pipfile /app/
COPY ./manage.py /app/
COPY ./requirements.txt /app/

RUN apk --update add uwsgi-python3 make bash \
               gcc libffi libffi-dev musl-dev linux-headers python3-dev build-base pcre-dev \
    && pip install -r /app/requirements.txt \
    && apk del gcc libffi libffi-dev musl-dev linux-headers python3-dev build-base pcre-dev \
    && rm -rf /var/cache/apk

COPY ./project /app/project

# link static files for web server
RUN ln -s /app/project/client/static /app/static \
    # run validation
    && set -x && cd /app && make lint test
