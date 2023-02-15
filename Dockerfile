FROM python:3.10-alpine

MAINTAINER dendihandian

WORKDIR /root

COPY crontab /etc/cron.d/crontab

COPY task.py /root/task.py

RUN crontab /etc/cron.d/crontab

RUN touch /root/service.log

CMD crond && tail -f /root/service.log