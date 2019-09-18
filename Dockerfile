FROM python
ENV MONGODB_URI=uri
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python app.py