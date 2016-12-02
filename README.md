# frozenbubble_config

# setup dev environment

## grab repo

    cd <somedir>
    git clone git@github.corp.openx.com:mobile/frozenbubble_config.git
    
## setup virtual environment

    sudo pip install virtualenv
    cd frozenbubble_config
    virtualenv env
    source env/bin/activate
        
## note: you will need to run activate before starting the django app
    
    pip install django
    ./manage migrate
    
## start the local server

    ./manaage runserver
    
## the REST service can be accessed at http://localhost:8000/frozenbubble/config/<device_id>

    [http://localhost:8000/frozenbubble/config/test]
    
## the Config interface can be accessed at

    [http://localhost:8000/frozenbubble/admin]

