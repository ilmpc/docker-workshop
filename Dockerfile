FROM python:3.11-alpine

WORKDIR /app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD server ./server

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--root-path", "/api"]
