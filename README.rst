=====
vdutyDjangoTutorial:s
=====

vdutyDjangoTutorials is a simple Django app to conduct Web-based vtutorials. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "vtutorials" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'vtutorials',
    ]

2. Include the vtutorials URLconf in your project urls.py like this::

    url(r'^vtutorials/', include('vtutorials.urls')),

3. Run `python manage.py migrate` to create the vtutorials models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a vtutorial (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/vtutorials/ to participate in the vtutorial.
