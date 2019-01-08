# Build:
#   docker build -t project .
#
# Run:
#   docker run -it -p 8000:8000 project

FROM python:3.6-alpine

ADD . /project

WORKDIR /project

RUN pip install -r requirements.txt

EXPOSE 8000/tcp

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
