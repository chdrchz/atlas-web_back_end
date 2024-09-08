#!/usr/bin/env python3
""" Module that contains a function that returns an
    obfuscated log message.
"""

import re
from typing import List


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
