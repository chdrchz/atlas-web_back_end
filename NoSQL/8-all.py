#!/usr/bin/env python3
""" Module that contains list_all
"""

def list_all(mongo_collection):
    """

    Args:
        mongo_collection: Mongo DB collection

    Returns:
       pymongo collection object: All documents in collection
    """
    return mongo_collection.find()