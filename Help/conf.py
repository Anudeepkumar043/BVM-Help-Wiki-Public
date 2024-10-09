# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'EPMO'
author = 'BVMDEV'

# -- General configuration ---------------------------------------------------
extensions = ['myst_parser']  # Use MyST-Parser for markdown support

# Allow both reStructuredText (.rst) and Markdown (.md)
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Set the master document (index.md)
master_doc = 'index'  # Make sure index.md exists in the correct directory

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
