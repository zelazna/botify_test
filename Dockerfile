# @TODO leverage docker cache
FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY . /code/
RUN scripts/install.sh
CMD [ "python", "manage.py", "runserver" ,"0.0.0.0:8080" ]
