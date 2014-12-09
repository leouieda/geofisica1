#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Leonardo Uieda'
SITENAME = u'Geof\xedsica 1 - gravimetria e magnetometria'
SITESUBTITLE = u'Bacharelado em Geologia - Universidade do Estado do Rio de Janeiro'
SITEURL = ''
RELATIVE_URLS = True

TIMEZONE = u'America/Sao_Paulo'
DEFAULT_LANG = u'pt'

PATH = '.'
ARTICLE_PATHS = ['lessons']
ARTICLE_URL = 'lessons/{category}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = PAGE_URL

STATIC_PATHS = [
    'images',
    'extra/favicon.png',
    ]
EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'},
    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
SUMMARY_MAX_LENGTH = 0

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary',
           'better_figures_and_images',
           'html_rst_directive',
           'render_math',
           ]
RESPONSIVE_IMAGES = False
FIGURE_NUMBERS = True
MATH = {'color': '#424242'}

THEME = 'theme'

INTERNALLINKS = [
    ['Sobre', 'index.html'],
    ['Ementa', 'ementa.html'],
    ['Gravimetria', 'category/gravimetria.html'],
    ['Magnetometria', 'category/magnetometria.html'],
    ]
EXTERNALLINKS = [
    ]


# This goes at the footer of the site
COPYRIGHT_NOTICE = """
<a rel="license"
 href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
><img alt="Creative Commons License" style="border-width:0"
 src="http://i.creativecommons.org/l/by/4.0/88x31.png"
/></a><br />
This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"
>Creative Commons Attribution 4.0 International License</a>.
"""
FOOTER = """
Powered by <a href="http://getpelican.com/">Pelican</a>
and <a href="http://python.org">Python</a>.
Source code at
<a
href="https://github.com/leouieda/geofisica1">github.com/leouieda/geofisica1</a>
"""
