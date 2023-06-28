FROM ubuntu:latest
LABEL authors="hasan"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek

RUN pip install --upgrade pip

WORKDIR  /app

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["top", "-b"]