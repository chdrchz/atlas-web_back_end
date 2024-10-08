#!/usr/bin/env python3
""" Python module
"""

def schools_by_topic(mongo_collection, topic):
    """ Returns a list of schools with a specific topic

    Args:
        mongo_collection pymonmgo collection obj: DB collection
        topic: topic to search
    """
    return mongo_collection.find({"topics": topic})