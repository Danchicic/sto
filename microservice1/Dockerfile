FROM python:3.13-slim
COPY . /mic1
WORKDIR /mic1
RUN ["pip3", "install", "fastapi", "uvicorn"]
EXPOSE 8121
CMD ["python", "main.py"]