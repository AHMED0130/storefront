FROM python:3.12.1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
#run both of them through docker-compose command >>
#RUN python manage.py migrate
#CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
