FROM python:3.4-alpine
ADD . /counter-app
WORKDIR /counter-app
RUN pip install -r requirements.txt
CMD ["python", "run.py"]
