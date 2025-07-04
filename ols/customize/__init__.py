"""Contains customization packages for individual projects (for prompts/keywords)."""

import importlib
import os

project = os.getenv("PROJECT", "noop")
metadata = importlib.import_module(f"ols.customize.{project}.metadata")
prompts = importlib.import_module(f"ols.customize.{project}.prompts")
keywords = importlib.import_module(f"ols.customize.{project}.keywords")
reranker = importlib.import_module(f"ols.customize.{project}.reranker")
filenames = importlib.import_module(f"ols.customize.{project}.filenames")
