# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt update -y && apt -y install build-essential git && git clone https://github.com/google/jsonnet.git && cd jsonnet && make
RUN pip install allennlp==2.2.0 allennlp-models==2.2.0
EXPOSE 8501
COPY . .
ENTRYPOINT ["streamlit", "run"]
CMD [ "main.py"]
