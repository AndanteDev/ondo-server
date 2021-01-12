FROM python:3.8
WORKDIR /code
COPY . /code/ 
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "db", "init"]
CMD ["python", "manage.py", "db", "migrate"]
CMD ["python", "manage.py", "db", "upgrade"]
CMD ["python", "manage.py", "run"]