FROM python
COPY * /app
WORKDIR /app
RUN ls
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python app.py