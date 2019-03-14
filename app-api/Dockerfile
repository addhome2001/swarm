FROM kennethreitz/pipenv

# set environment variables
ENV FLASK_APP=app/__init__.py

COPY . /app

CMD [ "gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "app:app" ]
