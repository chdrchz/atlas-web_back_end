#!/usr/bin/env python3

from pymongo import MongoClient

def nginx_stats():
    # Connect to database
    client = MongoClient('mongodb://localhost:27017/')

    # Access the 'logs' database and 'nginx' collection
    db = client.logs
    collection = db.nginx

    # Count the logs
    total_logs = collection.count_documents({})

    # Count the number of logs for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({"method": method}) for method in methods}
    status_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print the output
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_counts[method]}")
    print(f"{status_count} status check")

if __name__ == "__main__":
    nginx_stats()