FROM python:3.10

COPY ./requirements.txt /etc/requirements.txt

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r /etc/requirements.txt

COPY . /app
WORKDIR /app

#CMD python3 manage.py runserver
