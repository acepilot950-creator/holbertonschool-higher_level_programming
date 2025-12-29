#!/usr/bin/python3
"""
Module that provides a function to check if an object is an instance
of a class that inherited (directly or indirectly) from another class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, but is not an instance
    of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
