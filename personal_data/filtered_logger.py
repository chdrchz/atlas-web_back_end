#!/usr/bin/env python3
""" Module that obfuscates data

    Functions:
        - filter_datum: Obfuscates field data and
        returns a string with redacted Personal Data
    
    Classes: 
        - RedactingFormatter: Filters data
"""

import re
import logging
from typing import List


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
        """ Format log message by redacting specific fields
        """
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, log_message, self.SEPARATOR)


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
