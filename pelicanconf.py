from __future__ import unicode_literals

AUTHOR = 'Tierärzte Schaumburger Land'
SITENAME = 'Tierärzte Schaumburger Land'
SITEURL = ''
CC_LICENSE = 'CC-BY'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'
DEFAULT_DATE = 'fs'  # use filesystem date if not given in article
USE_FOLDER_AS_CATEGORY = True

THEME = 'medvets-theme'
BOOTSTRAP_NAVBAR_INVERSE = False
HIDE_SIDEBAR = True

# Some hand-crafted entries (links) in the main menu
# MENUITEMS = [('foo', 'http://foo.org')]

# Links to external partners
LINKS = []

DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = "Neues"

DISPLAY_TAGS_ON_SIDEBAR = False

DISPLAY_CATEGORIES_ON_SIDEBAR = False

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False

SOCIAL = None


###############################################################################
# Technical stuff ahead. You probably don't need to worry beyond this point.
###############################################################################

OUTPUT_PATH = "../html"  # relative to the pelicanconf.py file

# Always copy these to output, so they get uploaded.
STATIC_PATHS = ['images', '__downloads', 'custom-css/medvets.css']

# The name of the dir containing the static pages to put into the menu
# PAGE_PATHS = ['pages']

# The dir to process input files (relative to pelicanconf.py)
PATH = '.'

DEFAULT_PAGINATION = True

# We don't need a page listing the different authors
AUTHORS_SAVE_AS = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True  # Note: gets overwritten in production setup!

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'custom-css/medvets.css': {'path': 'static/medvets.css'}
}
CUSTOM_CSS = 'static/medvets.css'

SITELOGO = 'images/vetmed_logo.svg'
SITELOGO_SIZE = '25 em'

# The plugins to load
# Note, `hierarchy` is our own plugin for hierachic static pages.
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['hierarchy']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# STATIC_LANG_SAVE_AS = "{path}-{lang}"

# Extract title, slug and optionally the language from filename
# (Note: The file extension and the dot have already been stripped).
# The extraction of title, slug and lang from the file name avoids the most
# common "title not defined" error and makes defining :title and :slug
# and :lang in a page optional.
# Example file name: `Here-is-my-post-en.md`
# Will set both, title and slug to "Here-is-my-post" and the lang to "en"
# The `((?!-(en|de)).)+` part matches one or more (`+`) of any char (`.`) but
# not if the next chars are `-en` or `-de`.
# Use http://www.pyregex.com to test this Regex.
# FILENAME_METADATA = r'(?P<order>[0-9]*(_|-| ))?(?P<slug>(?P<title>((?!-(en|de)).)+))(-(?P<lang>(en|de)))?'
FILENAME_METADATA = r'(?P<order>[0-9]*(_|-| ))?(?P<slug>(?P<title>.+))?'
# FILENAME_METADATA = r'(?P<order>[0-9]*(_|-| ))?(?P<slug>(?P<title>))'
