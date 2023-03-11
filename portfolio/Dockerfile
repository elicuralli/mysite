FROM python:3.9.10-alpine3.14
WORKDIR /eli
RUN pip install --upgrade pip
RUN pip install flask
COPY . /eli
ENV FLASK_APP=app
CMD ["python", "scripts.py"]