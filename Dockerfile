FROM python:3.11.6-alpine3.18
RUN addgroup app && adduser -S -G app app
USER app
WORKDIR /app
COPY  pipfile pipfile.lock   /app/
RUN pip install pipenv
RUN pipenv install 
EXPOSE 8000
COPY . /app/
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver"]
