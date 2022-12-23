FROM python:3.11-alpine

WORKDIR /app

ADD requirements.txt .
RUN pip3 install -r requirements.txt

ADD main.py .

EXPOSE 8000

# CMD python -m uvicorn main:app --host 0.0.0.0
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]