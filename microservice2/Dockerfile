FROM python:3.13-slim
COPY . /mic2
WORKDIR /mic2
RUN ["pip3", "install", "fastapi", "uvicorn"]
EXPOSE 8120
CMD ["python", "main.py"]