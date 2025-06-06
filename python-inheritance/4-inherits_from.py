#!/usr/bin/python3
"""Module that provides a function to check if an object inherits
    from a specified class"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj inherits from a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
