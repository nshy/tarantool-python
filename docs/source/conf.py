# Tarantool python client library documentation build configuration file, created by
# sphinx-quickstart on Tue Nov 29 06:29:57 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath('.')), "src"))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.ifconfig', 'sphinx_paramlinks',
              'sphinx_favicon',]

autodoc_default_options = {
    'members': True,
    'inherited-members': True,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Tarantool python client library'
copyright = u'2011-2022, tarantool-python AUTHORS'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

import tarantool

# The short X.Y version.
version = tarantool.__version__
# The full version, including alpha/beta/rc tags.
release = tarantool.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

#html_style = 'style.css'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'sidebarwidth': '30%'}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Set up favicons with sphinx_favicon.
favicons = [
    {
        "rel": "icon",
        "static-file": "favicon/icon.svg",
        "type": "image/svg",
    },
    {
        "rel": "icon",
        "sizes": "16x16",
        "static-file": "favicon/icon-16x16.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "32x32",
        "static-file": "favicon/icon-32x32.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "96x96",
        "static-file": "favicon/icon-96x96.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "128x128",
        "static-file": "favicon/icon-128x128.png",
        "type": "image/png",
    },
    {
        "rel": "icon",
        "sizes": "196x196",
        "static-file": "favicon/icon-196x196.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "57x57",
        "static-file": "favicon/apple-touch-icon-57x57.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "60x60",
        "static-file": "favicon/apple-touch-icon-60x60.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "72x72",
        "static-file": "favicon/apple-touch-icon-72x72.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "76x76",
        "static-file": "favicon/apple-touch-icon-76x76.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "114x114",
        "static-file": "favicon/apple-touch-icon-114x114.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "120x120",
        "static-file": "favicon/apple-touch-icon-120x120.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "144x144",
        "static-file": "favicon/apple-touch-icon-144x144.png",
        "type": "image/png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "152x152",
        "static-file": "favicon/apple-touch-icon-152x152.png",
        "type": "image/png",
    },
]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Tarantoolpythonclientlibrarydoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Tarantoolpythonclientlibrary.tex', u'Tarantool python client library Documentation',
   u'tarantool-python AUTHORS', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'tarantoolpythonclientlibrary', u'Tarantool python client library Documentation',
     [u'tarantool-python AUTHORS'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Tarantoolpythonclientlibrary', u'Tarantool python client library Documentation',
   u'tarantool-python AUTHORS', 'Tarantoolpythonclientlibrary', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('http://docs.python.org/', None),
    'msgpack': ('https://msgpack-python.readthedocs.io/en/latest/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'pytz': ('https://pytz.sourceforge.net/', None),
}


autoclass_content = "both"
