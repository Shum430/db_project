FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

# Collect static files
#RUN python manage.py collectstatic --noinput

# Run the application
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "db_project.wsgi:application"]
CMD ["python", "manage.py", "runserver"]
