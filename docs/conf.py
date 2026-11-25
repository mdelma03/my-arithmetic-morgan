project = "my-arithmetic-morgan"
author = "Morgan"
release = "0.2.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

# Configuration de Napoleon pour le format NumPy uniquement
napoleon_numpy_docstring = True
napoleon_google_docstring = False
napoleon_include_init_with_doc = False

language = "fr"
html_theme = "furo"