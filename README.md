# ccm-back-end-django
# Setup

The first thing to do is to clone the repository:

    git clone https://github.com/carbonmap/ccm-back-end-django.git
    cd ccm-back-end-django

To create a virtual environment python has a built-in package venv (note that python3 is required):

            python -m venv myenvname
to activate:

            source myenvname/bin/activate

Switch to the project directory:

                    cd carbon/


Then install the dependencies:

            (myenvname)$ pip install -r requirements.txt



Perform database migration:

            python manage.py migrate

Note that you need to [create superuser](https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser):

            python manage.py createsuperuser

Run your project locally.

            python manage.py runserver