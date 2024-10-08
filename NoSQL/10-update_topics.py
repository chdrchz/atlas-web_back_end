#!/usr/bin/env python3
""" Python module
"""


def update_topics(mongo_collection, name, topics):
    """ Updates all document topics

    Args:
        mongo_collection pymongo collection obj: DB collection
        name: name of the school to update
        topics: topics for the school

    Returns:
        pymongo collection object: DB collection w/ updated topics
    """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})