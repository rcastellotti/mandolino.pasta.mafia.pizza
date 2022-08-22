
FROM python:alpine
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", ":8080", "--workers", "2", "mpmp:app"]
