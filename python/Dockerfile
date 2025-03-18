FROM python:3.10

WORKDIR /app

RUN apt-get update && \
    apt-get install -y apt-utils sqlite3 libsqlite3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

# FastAPI port
EXPOSE 8000

# FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
