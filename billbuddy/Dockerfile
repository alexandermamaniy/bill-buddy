FROM python:3.9
RUN mkdir /billbudy
WORKDIR /billbudy
COPY . /billbudy/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /service/service/
RUN python manage.py makemigration
RUN python manage.py migrate
RUN python manage.py loaddata seeders/data.json
RUN python manage.py spectacular --file schema.yml
RUN python manage.py runserver
