# BillBuddy
Application to manage share bill in apartments and houses

# Download, configuration and libraries installation
```
- git clone https://github.com/akey96/resume-manage.git
- virtualenv --python=python3.9.13 venvs
- source env/bin/activate
- pip install -r requirements.txt
- cd billbuddy/
```

# Run migration and server
```
- python manage.py makemigration
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
```


# Generate and restore backup
```
- python manage.py dumpdata users  > seeders/data.json
- python manage.py loaddata seeders/data.json
```

# Run test
```
- python manage.py test
```
# Run interactive mode
```
- python manage.py shell
```
# Compile