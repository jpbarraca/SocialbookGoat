FROM python:3.11

WORKDIR /app

COPY app/ .

RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/database
RUN chown -R root:root /app/database
RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
