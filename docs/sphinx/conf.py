import sys
from pathlib import Path

sys.path.insert(0, str(Path("..", "..", "vematch").resolve()))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "VeMatch"
copyright = "2024, Gabriel Soares Baptista"
author = "Gabriel Soares Baptista"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

html_baseurl = 'https://gsoaresbaptista.github.io/VeMatch/'
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.githubpages"
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ["_static"]
html_logo = "_static/logo/purple.svg"
html_favicon = "https://raw.githubusercontent.com/gsoaresbaptista/VeMatch/main/docs/_static/purple.svg"
html_theme_options = {
    "accent_color": "iris",
    "dark_code": True,
    "nav_links": [
        {
            "title": "VeMatch",
            "url": "https://gsoaresbaptista.github.io/VeMatch/"
        },
    ]
}
