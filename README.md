# ccm-back-end-django
# Setup

The first thing to do is to clone the repository:

    git clone https://github.com/carbonmap/ccm-back-end-django.git
    cd ccm-back-end-django

To create a virtual environment python has a built-in package venv (note that python3 is required):

    python -m venv venv

to activate:

    source venv/bin/activate

Switch to the project directory:

    cd carbonmap_project/

Then install the dependencies (note that mysql must be installed for this to complete):

    pip install -r requirements.txt

Copy the environment settings (you can use the default for local installation):

    cp .env-sample .env

Perform database migration:

    python manage.py migrate

Note that you need to [create superuser](https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser):

    python manage.py createsuperuser

Run your project locally.

    python manage.py runserver
