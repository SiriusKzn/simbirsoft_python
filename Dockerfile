FROM python:3
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
COPY requirements.txt ./
RUN pip install -r requirements.txt
