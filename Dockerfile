FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Use SQLite settings for Docker
ENV DJANGO_SETTINGS_MODULE=news_app.settings_docker

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

