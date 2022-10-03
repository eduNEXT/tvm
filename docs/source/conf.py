# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TVM Documentation'
copyright = '2022, eduNEXT'
author = 'eduNEXT'
release = 'v2.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinxcontrib.yt",
    "sphinxcontrib.images",
    "sphinx_panels",
    "sphinxcontrib.contentui",
    "sphinx_copybutton",
    "sphinx.ext.graphviz",
    "sphinxcontrib.mermaid",
    "recommonmark",
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# eduNEXT configuration
html_logo = '_static/Knowledge_Base_logo.png'
extra_navbar_content = """
<hr/><br/>

<a class='external' href='https://bitbucket.org/edunext/edunext-documentation/src/master/' target='_blank'>About the 
project in bitbucket:</a><br/> 


"""

html_theme_options = {
    "repository_url": "https://github.com/eduNEXT/edunext-internal-documentation.git",
    "repository_branch": "main",
    "path_to_docs": "source",
    "use_edit_page_button": True,
    "logo_only": False,
    "extra_navbar": extra_navbar_content,
    "home_page_in_toc": True,
    "show_navbar_depth": 1,
    "use_repository_button": True,
    "use_issues_button": True
}

html_sidebars = {'**': ["sidebar-logo.html", "search-field.html", "sbt-sidebar-nav.html"]}

# For custom styles
images_config = {
    "default_image_width": "100%",
}

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
]

html_js_files = [
    "_js/custom.js",
]

togglebutton_hint = "Show"
togglebutton_hint_hide = "Hide"

# Panels conf
panels_add_bootstrap_css = False
# html_title = ""