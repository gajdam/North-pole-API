FROM python:3.10.4-slim
WORKDIR /app
COPY main.py requirements.txt /app/
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]