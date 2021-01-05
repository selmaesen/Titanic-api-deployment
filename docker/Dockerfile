FROM python:3.8
COPY requirements.txt .
RUN pip install --upgrade -r requirements.txt

RUN mkdir /app
RUN mkdir /app/docker
RUN mkdir /app/pipeline

COPY . /app

WORKDIR /app

CMD ["python", "app.py"]
