#!/usr/bin/env python3
""" Module that obfuscates data

    Functions:
        - filter_datum():
            Obfuscates field data and
            returns a string with redacted Personal Data
        - get_logger():
            Creates a logger obj w/ all pertinent data
            and returns a logging.Logger obj that
            filter_datum will use
        - get_db():
            Returns a secure connection to a database
        - main():
            puts it all together and further formats the output string
            
    Classes:
        - RedactingFormatter: Filters data
"""

import datetime
import os
import re
import logging
from typing import List
from mysql.connector import connect, MySQLConnection

# Environment variables for database connection
username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
password = os.getenv('PERSONAL_DATA_DB_PASSWORD', 'root')
host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
database = os.getenv('PERSONAL_DATA_DB_NAME', 'my_db')

# Data for formatting fields list
PII_FIELDS = ("name", "email", "password", "phone", "ssn")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor method
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Function that formats log message by redacting specific fields
        """
        # Super here to get the fields from the constructor method
        log_message = super().format(record)

        return filter_datum(
                self.fields, self.REDACTION, log_message, self.SEPARATOR)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """ Function that obfuscates data fields.

        Args:
            - fields: the value type of data to be osfucated
            - redaction: what to replace the field data with
            - message: the string to parse
            - seperator: what each field is separated by to parse

        Return:
            - the message obfuscated
    """
    pattern = rf'({("|".join(fields))})=([^;]*?)(?={separator}|$)'
    return re.sub(pattern, lambda match: f"{match.group(1)}={redaction}", message)


def get_logger() -> logging.Logger:
    """ Function that returns a logging object
    """
    # create a new logger
    logger = logging.getLogger("user_data")

    # Set level of logger to INFO (20)
    logger.setLevel(logging.INFO)

    # Do not allow propogation to other loggers
    logger.propagate = False

    # Handle output to console
    handler = logging.StreamHandler()

    # Get that data formatted + link the handler and data together
    formatter = RedactingFormatter(fields=PII_FIELDS)
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger


def get_db() -> MySQLConnection:
    """ Connects to a db using env variables

        Return:
            - MySQL connection
    """
    db = connect(
        user=username,
        password=password,
        host=host,
        database=database
    )
    return db

def main() -> None:
    """ Main function 
    """
    # Establish database connection
    db = get_db()

    sensitive_fields = {
        "name": "name",
        "email": "email",
        "phone": "phone",
        "ssn": "ssn",
        "password": "password"
    }

    try:
        # Create a cursor object
        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT * FROM users")

        # Fetch all rows
        users = cursor.fetchall()

        for user in users:
           user_dict = {
                "name": user[0],
                "email": user[1],
                "phone": user[2],
                "ssn": user[3],
                "password": user[4],
                "ip": user[5],
                "last_login": user[6],
                "user_agent": user[7]
            }
            
        # Format the user data as a string
        user_str = '; '.join(f"{key}={value}" for key, value in user_dict.items())
        
        # Redact sensitive information
        filtered_user = filter_datum(sensitive_fields.keys(), "***", user_str, ";")
        print(f"[HOLBERTON] user_data INFO {datetime.datetime.now()}: {filtered_user}")

    except Exception as e:
        print(f"Error occurred while fetching data from database: {e}")
    
    finally:
        # Ensure the cursor is closed
        if cursor:
            cursor.close()
        
        # Ensure the database connection is closed
        if db:
            db.close()

if __name__ == "__main__":
    main()
