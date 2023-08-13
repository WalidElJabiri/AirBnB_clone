#!/usr/bin/python3
"""
Module to initialize and reload the storage for the application.
"""

from .engine.file_storage import FileStorage

"""
Initialize the storage and reload existing data
"""
storage = FileStorage()
storage.reload()
