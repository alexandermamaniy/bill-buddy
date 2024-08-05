FROM python:3.9
RUN mkdir /billbudy
WORKDIR /billbudy
COPY . /billbudy/
WORKDIR /billbudy/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN ls && pwd
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py loaddata seeders/data.json
RUN python manage.py spectacular --file schema.yml
EXPOSE 8000
CMD python manage.py runserver
