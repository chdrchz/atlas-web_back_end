#!/usr/bin/env python3
""" Module that contains a function that returns an
    obfuscated log message.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str):
    """ Function that obfuscates username and password fields.
    
        Args: 
            - fields: the value type of data to be osfucated
            - redaction: what to replace the field data with
            - message: the string to parse
            - seperator: what each field is separated by to parse
        
        Return:
            - the message obfuscated
    """
    pattern = r'(' + '|'.join(fields) + r')=([^' + re.escape(separator) + r']*)'
    
    return re.sub(pattern, redaction, message)
