FROM python:3-onbuild AS builder

COPY . /usr/src/app

CMD [ "gunicorn", "-b", ":80", "api:app" ]
