# BillBuddy
Application to manage share bill in apartments and houses

## System Dependencies
- docker
- docker-compose

## Project Download
```
- git clone https://github.com/alexandermamaniy/bill-buddy.git
- cd billbuddy/
```

## Develop stage
This stage allows developers make changes to the code and reflects the updates in real time.
```
- docker-composer -f docker-compose.override.yml build
- docker-composer -f docker-compose.override.yml up
```

### Run migration and server
You can run generate the migrations and apply them and also create a superuser in order to crowded
```
- docker-composer -f docker-compose.override.yml exec web python manage.py makemigrations core users buddy_profiles buddy_groups buddy_expenses
- docker-composer -f docker-compose.override.yml exec web python manage.py migrate
- docker-composer -f docker-compose.override.yml exec web python manage.py createsuperuser
- docker-composer -f docker-compose.override.yml exec web python manage.py runserver
```


### Generate and restore backup
If you want to populate the database by seeders, you must not create a superuser by commands.  
```
- docker-composer -f docker-compose.override.yml exec web python manage.py dumpdata > seeders/data.json
```
```
- docker-composer -f docker-compose.override.yml exec web web python manage.py flush --noinput
- docker-composer -f docker-compose.override.yml exec web web python manage.py dumpdata > seeders/data2.json
```


### Run test
```
- docker-composer -f docker-compose.override.yml exec web python manage.py test
```
### Run interactive mode
```
- docker-composer -f docker-compose.override.yml exec web python manage.py shell
```
### Generate Scheme for Swagger
If you make any changes in the models, must run this command to update the Swagger's schemas  
```
- docker-composer -f docker-compose.override.yml exec web python manage.py spectacular --file schema.yml 
```
then go to http://localhost:8000/api/schema/docs/#/


## Deploy stage