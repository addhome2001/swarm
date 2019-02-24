FROM kennethreitz/pipenv

# set environment variables
ENV FLASK_APP=app/__init__.py

COPY . /app

CMD [ "flask", "run", "--host=0.0.0.0", "--port=8000" ]
