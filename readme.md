# Create virtual env and install

python -m venv env
source env/bin/activate

pip install djangorestframework

pip freeze > requirements.txt

# Start a new project and app

django-admin startproject config .

python manage.py startapp <name_of_app>

# Register apps in config/settings.py

installed apps, register;
- "rest_framework"
- "<name_of_app>"

#  Models

- wire up models
- run migrations
- create superuser adn populate db

# Serilaizers 
- ModelSerializers (easy way out)
- Plain Serializer. (want more control)

# Views (Four levels of Abstraction)
- Level 1 @api_view (Function based views)
- Level 2 APIView (Class-based)
- Level 3 Generic Views
- Level 4 ViewSets (most concise)

# URLs & Routers 
- Manual URL wiring (for APIView and generics)
- Router (for ViewSets)


