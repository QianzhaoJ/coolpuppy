# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import mock
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = 'coolpup.py'
copyright = '2020, Ilya M. Flyamer'
author = 'Ilya M. Flyamer'

# The full version, including alpha/beta/rc tags
release = '0.9.3'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              'nbsphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.napoleon',
              'sphinxarg.ext',
              'm2r'
              ]


MOCK_MODULES = ['cooltools',
                'numpy',
                'scipy',
                'scipy.linalg',
                'Cython',
                'matplotlib',
                'pandas',
                'h5py',
                'cooler',
                'pysam',
                'natsort',
                'yaml'
                ]

for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = mock.Mock()

# autodoc_mock_imports = [
#     'cooltools',
#     'numpy',
#     'scipy',
#     'Cython',
#     'matplotlib',
#     'pandas',
#     'h5py',
#     'cooler',
#     'pysam',
#     'natsort'
# ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

add_module_names = True

master_doc = 'index'

def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)
    app.add_stylesheet('my_theme.css')

source_suffix = ['.rst', '.md', '.ipynb']
html_favicon = 'favicon.ico'