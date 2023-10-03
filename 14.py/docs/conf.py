import sys
import os

sys.path.insert(0, os.path.abspath('..'))

project = '14.py'
copyright = '2023, Yaroslav'
author = 'Yaroslav'

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'nature'
html_static_path = ['_static']
