#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from pathlib import Path
import sys
sys.path.insert(0, str(Path.cwd()))
from contentblocks import *
sys.path.pop(0)

PATH = 'content'
AUTHOR = 'Blind Pandas Team'
SITENAME = 'Blind Pandas'
TIMEZONE = 'Africa/Khartoum'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY  = 'Uncategorised'
SITESUBTITLE = "Free & high quality software for the blind and visually impaired "
SITEURL = 'https://blindpandas.com'
RELATIVE_URLS = True
DEVELOPMENT = True
LOAD_CONTENT_CACHE = False

# Re-map URLs
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
ARTICLE_LANG_URL = 'blog/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = 'blog/{slug}-{lang}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_LANG_URL = '{slug}-{lang}.html'

# We don't need to generate the following
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DRAFT_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''
DRAFT_PAGE_LANG_SAVE_AS = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 5

# Custom theme
THEME  = Path.cwd() / "theme"
THEME_STATIC_DIR = 'theme'
# Static files
STATIC_PATHS = ['static', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'static/*': {'path': 'static/'},
    'static/images/favicon.ico': {'path': 'favicon.ico'},
}

# Plugins
PLUGIN_PATHS = ('plugins',)
PLUGINS = ('seo', 'htmlcompress',)

# SEO
SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = True
IMAGE_PATH = 'static/images'

# OG properties
OG_LOCALE = "en_US"
HEADER_COVER = "static/images/logo512x512.png"
