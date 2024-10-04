#!/usr/bin/env python3
""" Module that contains a class Cache
"""

import uuid
import redis
from functools import wraps
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """ Counts the number of times a method from the cache
        class is called.

    Args:
        method (Callable): the wrapper method that counts instances

    Returns:
        Callable: Calls itself over and over again
    """
    # Key is qualifiable
    key = method.__qualname__
    
    # Count how many times the method is called
    @wraps(method)
    def wrapper(*args, **kwargs):
        
        # Same as i++
        self._redis.incr(method.__qualname__)
        return method(*args, **kwargs)

    return wrapper


class Cache: 
    """ Class Cache
    """

    def __init__(self):
        """ init method
        """
        # Redis connection iunstance
        self._redis = redis.Redis()

        # Flush the database
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generates a random uuid and stores the key in redis

        Args:
            data (_type_): data to be stored with key

        Returns:
            str: a key
        """
        # Get the key
        key = str(uuid.uuid4())

        # Store the key
        # Returning here causes a bool response
        self._redis.set(key, data)

        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int]]] = None
                ) -> Optional[Union[str, int]]:
        """ Retrieve data from Redis and optionally apply a conversion function.

        Args:
            key (str): The key to retrieve from Redis.
            fn (Optional[Callable[[bytes], Union[str, int]]]): Optional conversion function.

        Returns:
            Optional[Union[str, int]]: The converted data, or None if the key does not exist.
        """
        # Get the value of the key
        value = self._redis.get(key)

        # Meaning the key is empty
        if value is None:
            return None;

        # Meaning the callable function was given
        if fn is not None:
            return fn(value)

        # Return the value cause fn was not given
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ Retrieve data as a string from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[str]: The retrieved string data, or None if the key does not exist.
        """

        # Convert byte string to regular string
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """ Retrieve data as an integer from Redis.

        Args:
            key (str): The key to retrieve from Redis.

        Returns:
            Optional[int]: The retrieved integer data, or None if the key does not exist.
        """

        # Convert byte string to integer
        return self.get(key, lambda x: int(x))