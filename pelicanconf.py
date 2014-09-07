# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thierry Carrez'
SITENAME = u'ttx:reloaded'
SITEURL = 'http://ttx.re'
GOOGLE_ANALYTICS = 'UA-54541847-1'

PATH = 'content'
THEME = './theme'

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/keybase.txt']
EXTRA_PATH_METADATA = { 'extra/CNAME': {'path': 'CNAME'},
                        'extra/keybase.txt': {'path': 'keybase.txt'} }

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/tcarrez'),)
TWITTER_USERNAME = "tcarrez"

DEFAULT_PAGINATION = 5
TYPOGRIFY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
