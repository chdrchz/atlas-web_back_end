#!/usr/bin/env python3
""" Python module
"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document

    Args:
        mongo_collection pymongo collection obj: DB collection

    Returns:
        pymongo collection obj: collection including new document
    """
    return mongo_collection.insert_one(kwargs).inserted_id