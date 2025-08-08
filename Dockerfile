FROM python:3.12-slim

WORKDIR /app

COPY . .

EXPOSE 80

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "./src/main.py"]
