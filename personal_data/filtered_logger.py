#!/usr/bin/env python3
""" Module that obfuscates data

    Functions:
        - filter_datum:
            Obfuscates field data and
            returns a string with redacted Personal Data
        - get_logger():
            Creates a logger obj w/ all pertinent data
            and returns a logging.Logger obj that
            filter_datum will use

    Classes:
        - RedactingFormatter: Filters data
"""

import os
import re
import logging
from typing import List
import mysql.connector

# Environment variables for database connection
username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
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
    pattern = rf'({"|".join(fields)})=([^ {re.escape(separator)}]*)'

    return re.sub(pattern, lambda match: match.group(1)+'='+redaction, message)


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Connects to a db using env variables

        Return:
            - MySQL connection
    """
    db = mysql.connector.connect(
        host=os.getenv("PERSONAL_DATA_DB_HOST"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )
    return db


def main() -> None:
    """ Main function
    """
    # Get database connection
    db = get_db()
    
    # Create a cursor obj and add it to the db connection
    with db.cursor() as cursor:

        # Execute the SQL command
        cursor.execute("SELECT * FROM users")

        # Grab all the data
        users = cursor.fetchall()
    
    # Fields to regex
    sensitive_fields = [
        "name",
        "email",
        "phone",
        "ssn",
        "password"
    ]
    
    for user in users:
        filtered_data = filter_datum(sensitive_fields, "***", user, ";")
        
        # Log that data
        logger = get_logger() # Create a logger obj
        logger.info(filtered_data)

# Only main will run
if __name__ == "__main__":
    main()