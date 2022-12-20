=====
Simple_Blog
=====

Simple_Blog is a Django app for a simple blog application

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'simple_blog',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('blog/', include('simple_blog.urls')),

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to post stuff

5. Visit http://127.0.0.1:8000/blog/ to view posts