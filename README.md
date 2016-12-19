# frozenbubble_config

# setup dev environment

## grab repo

    cd <somedir>
    git clone git@github.corp.openx.com:mobile/frozenbubble_config.git
    
## install packages

    sudo yum install -y sqlite-devel
    
## setup virtual environment

    sudo pip install virtualenv
    cd frozenbubble_config
    virtualenv env
    source env/bin/activate
        
## note: you will need to run activate before starting the django app
    
    pip install django
    python manage.py migrate
    
## note2: python might need to be reinstalled/recompiled after downloading sqlite-devel in order to import sqlite3
   
## create superuser name and password - this will be used to log in to the config interface

    ./manage createsuperuser

## start the local server

    ./manage runserver
    
## the REST service can be accessed at (test is an example device id)

http://localhost:8000/frozenbubble/config/test
    
## the Config interface can be accessed at

http://localhost:8000/frozenbubble/admin

