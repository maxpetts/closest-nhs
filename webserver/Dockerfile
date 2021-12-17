FROM python:3-onbuild AS builder

COPY . /usr/src/app

# CMD [ "gunicorn", "-b", ":80", "--workers=2", "--threads=4", "api:app" ]
CMD ["python3", "api.py"]
