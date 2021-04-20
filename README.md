# django-rest-api-project-structure-template
A sample project structure template for Django RESTful API with  Boilerplate Authentication app

# Project Structure 

.                                                        # project root
├── API                                                
│   ├── apps                                             # app directory
│   │   ├── authentication
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── __init__.py
│   │   │   ├── migrations
│   │   │   ├── models.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── common                                       # common resources/utilities reusable across apps
│   │   │   ├── base.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── config                                           # configuration directory
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings
│   │   │   ├── base.py                                  # default django settings
│   │   │   ├── __init__.py
│   │   │   ├── local.py                                 # local dev settings
│   │   │   ├── production.py                            # production/deploying settings
│   │   │   └── test.py                                  # test setting
│   │   ├── urls.py                                      # project url entry point
│   │   └── wsgi.py                                      # project app entry point
│   └── tests
│       ├── authentication                               # test directory for authentication app
│       │   └── __init__.py
│       └── fixtures                                     # pytest fictures directory
│           └── __init__.py
├── manage.py                                            
├── Procfile
├── README.md
├── runtime.txt
└── static                                              # django static dir

# requirements
 - see requirements.txt file
 