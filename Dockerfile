FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

RUN python manage.py collectstatic --noinput

ENV PYTHONUNBUFFERED=1
ENV DEBUG=False

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]