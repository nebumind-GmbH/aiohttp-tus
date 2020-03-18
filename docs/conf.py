#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aiohttp-tus documentation build configuration file, created by
# sphinx-quickstart on Sun May 14 20:32:17 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import re
import sys
from pathlib import Path


rel = Path(__file__).parent.parent
sys.path.insert(0, str(rel))

INIT_PY = (rel / "aiohttp_tus" / "__init__.py").read_text()
VERSION = re.findall('__version__ = "([^"]+)"', INIT_PY)[0]


extensions = [
    "alabaster",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"

project = "aiohttp-tus"
description = "tus.io server implementation for aiohttp.web applications"
copyright = "2020, Pylot"
author = "Igor Davydenko"

version = ".".join(VERSION.split(".")[:2])
release = VERSION

language = "en"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

html_theme = "alabaster"
html_theme_options = {
    "logo_name": True,
    "description": description,
    "github_user": "pylotcode",
    "github_repo": project,
    "github_banner": True,
    "github_button": True,
    "github_type": "star",
    "fixed_sidebar": True,
}
html_static_path = ["_static"]
html_sidebars = {"**": ["about.html", "localtoc.html", "searchbox.html"]}

htmlhelp_basename = "aiohttp-tusdoc"
latex_elements = {}
latex_documents = [
    (master_doc, "aiohttp-tus.tex", "aiohttp-tus Documentation", "Pylot", "manual",)
]

man_pages = [(master_doc, "aiohttp-tus", "aiohttp-tus Documentation", [author], 1,)]

texinfo_documents = [
    (
        master_doc,
        "aiohttp-tus",
        "aiohttp-tus Documentation",
        author,
        "aiohttp-tus",
        description,
        "Miscellaneous",
    )
]

intersphinx_mapping = {
    "https://docs.python.org/3/": None,
    "https://aiohttp.readthedocs.io/en/stable/": None,
}
