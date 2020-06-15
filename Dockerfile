FROM python:3.6-slim
COPY ./main.py /deploy/
COPY ./templates /deploy/templates/
COPY ./static /deploy/static/
COPY ./requirements.txt /deploy/
COPY ./nb_trained_model.pickle /deploy/
COPY ./vectorizer.pickle /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "main.py"]
CMD flask run --host=0.0.0.0
# to run for first time: docker run -d -p 5000:5000 <image name(news-classifier-app)
# to stop: docker stop <container-name> and restart with docker start <container-name>