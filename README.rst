Django-photos
=============

the goal of django-photos is to provide a basic app that can be used to add
photo/gallery functionality to a model or site. This is in keeping with the
'do one thing well' idea of django and DRY.

Models provided
---------------

django-photos currently provides two models:

- Photo ( a basic model that stores and image, title, description, creation
  time)
- Gallery ( title, description, manytomany(Photo) )

The power of django-photos comes in integration; with easy-to-add predefined
widgets and form handling, creating a "Blog entry with gallery" could not be
easier.
