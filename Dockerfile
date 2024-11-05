FROM python:3.10.15-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
