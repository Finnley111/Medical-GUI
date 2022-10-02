# syntax=docker/dockerfile:1

FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


# Install Tkinter
RUN apt-get install tk -y

WORKDIR /app
COPY 20210616_1.csv .

WORKDIR /app
COPY GUI_heart_lab_v6.py GUI_heart_lab_v6.py

ENV DISPLAY=gui


CMD [ "python3", "./GUI_heart_lab_v6.py"]