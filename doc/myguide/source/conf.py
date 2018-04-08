# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys, os
#sys.path.append(os.path.abspath('_ext'))
#extensions = ['rstjinja']



#html_context = {
#}

# import sys
# import os
# import ablog

# sys.path.append(os.getcwd())  # noqa
# sys.path.insert(0, os.path.abspath('_ext'))

# from core import rstjinja


# -- Project information -----------------------------------------------------

project = u'Docs as Code'
copyright = u'2018, Frank Kloeker'
author = u'Frank Kloeker'

# The short X.Y version
#version = u''
# The full version, including alpha/beta/rc tags
#release = u'1.1'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.md' ]

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

html_theme_options = {
    'footerbgcolor': '#ffffff',
    'footertextcolor': '#03a6d7',
    'sidebarbgcolor': '#03a6d7',
    'sidebarbtncolor': '#ededed',
    'sidebartextcolor': '#eeeeee',
    'sidebarlinkcolor': '#3c3c3c',
    'relbarbgcolor': '#d0d0d0',
    'relbartextcolor': '#5c5c5c',
    'relbarlinkcolor': '#3c3c3c',
    'bgcolor': '#ffffff',
    'textcolor': '#5c5c5c',
    'linkcolor': '#222222',
    'visitedlinkcolor': '#2c2c2c',
#    'headbgcolor':
#    'headtextcolor':
#    'headlinkcolor':
    'codebgcolor': '#ededed',
    'codetextcolor': '#505050',
}


# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Docs as codedoc'


# -- Options for LaTeX output ------------------------------------------------

# latex_engine = 'xelatex'
# latex_elements = {
#     'fontpkg': r'''
# \setmainfont{DejaVu Serif}
# \setsansfont{DejaVu Sans}
# \setmonofont{DejaVu Sans Mono}
# ''',
#     'preamble': r'''
# \usepackage[titles]{tocloft}
# \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
# \setlength{\cftchapnumwidth}{0.75cm}
# \setlength{\cftsecindent}{\cftchapnumwidth}
# \setlength{\cftsecnumwidth}{1.25cm}
# ''',
#     'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
#     'printindex': r'\footnotesize\raggedright\printindex',
# }
# latex_show_urls = 'footnote'

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
#latex_documents = [
#    (master_doc, 'Docs as code.tex', u'Docs as Code Documentation',
#     u'Frank Kloeker', 'manual'),
#]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'docsascode', u'Docs as Code Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Docs as code', u'Docs as Code Documentation',
     author, 'Docs as code', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None}

intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'sphinx': ('http://www.sphinx-doc.org/en/master/', None)
} 

locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# -- Hieroglyph Slide Configuration ------------
extensions += ['hieroglyph']
slide_theme = 'single-level'
slide_levels = 3
slide_numbers = True
slide_link_to_html = True
slide_link_html_to_slides = True
slide_theme_options = {
    'custom_css': 'custom.css',
}
