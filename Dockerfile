FROM python:3.10-alpine
EXPOSE 8000
COPY . /opt/worker
WORKDIR /opt/worker
RUN pip install -r requirements.txt
ENTRYPOINT python /opt/worker/worker.py