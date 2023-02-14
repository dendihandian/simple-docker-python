FROM python:3.10-slim

RUN apt-get update && apt-get -y install cron vim

WORKDIR /root

COPY crontab /etc/cron.d/crontab

COPY task.py /root/task.py

CMD ["cron", "-f"]
