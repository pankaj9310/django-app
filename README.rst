nimoy
======


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------
Setting project on local
^^^^^^^^^^^^^^^^^^^^^
* set database name and password in config/settings/base.py @line 128.
* set email id and password in config/settings/base.py @line 34, 35::

	$ sudo apt-get install python python-dev python-pip virtualenv
	$ virtualenv venv_nimoy
	$ source venv_nimoy/bin/activate
	$ pip install -r requirements/local.txt
	$ python manage.py makemigrations
	$ python manage.py migrate
	$ python manage.py createsuperuser 
	$ python manage.py runserver


Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.
* To craete a user using social network, first register that app on website and find client id and client secret. Register socail network in django using admin panel add client id and client secret. 
* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser
* After login User can create project and task
* User can update project and task
For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

  $ py.test


Deployment
----------

The following details how to deploy this application.



