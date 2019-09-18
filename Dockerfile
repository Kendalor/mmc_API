FROM python
ADD api app
ADD database app
COPY app.py app/
COPY logging.conf app/
COPY requirements.txt app/
COPY settings.py app/
WORKDIR /app
RUN ls
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python app.py