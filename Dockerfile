FROM python
ENV MONGODB_URI
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python run.py -uri $MONGODB_URI