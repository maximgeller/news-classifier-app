FROM python:3.6-slim
COPY ./main.py /deploy/
COPY ./requirements.txt /deploy/
COPY ./nb_trained_model.pickle /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "main.py"]