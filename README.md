# MathEasier

SETUP:

Make sure you have postgres installed (https://www.postgresql.org/download/) and create a new db called "MathEasier"

In your virtual environment, in the root directory (same as manage.py), run pip install -r requirements.txt to install the app requirements to the virtual environment.

Add the proper .env file with the environmental/secret variables in the root (same location as manage.py)

Directory map for Django newcomers:

- character_sheet - self-contained; holds all info relating to the Character Sheet app itself.
-- Contains main template (html page) to serve Angular
-- Also contains views (controllers) and serializers for API endpoints to use with Angular
-- Also contains models and db migrations to do with the Character Sheet app.
- math_easier - main application setup
-- Contains main settings, wsgi (for heroku), and admin settings and pages.
- mathEasierAngular - main Angular app
-- Contains entirety of math_easier Angular app, including components and services
- static
- staticfiles

## Building locally:

Running Django: 
`python manage.py runserver`
Angular: 
`ng build --prod --output-path ../static/ang --watch --output-hashing none`