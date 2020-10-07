#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Blind Pandas Team'
SITENAME = 'Blind Pandas'
SITEURL = 'https://blindpandas.com'

PATH = 'content'

TIMEZONE = 'Africa/Khartoum'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# SEO
SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = False  # To disable this feature
IMAGE_PATH = 'images'
THUMBNAIL_KEEP_NAME = True
THUMBNAIL_KEEP_TREE  = True

# Static files
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
