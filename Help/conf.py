# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'EPMO'
author = 'BVMDEV'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',  # Replaces recommonmark for better Markdown support
]

# Allow both reStructuredText (.rst) and Markdown (.md)
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # You can choose a theme of your choice
