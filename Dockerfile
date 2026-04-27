FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY templates/ templates/
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
