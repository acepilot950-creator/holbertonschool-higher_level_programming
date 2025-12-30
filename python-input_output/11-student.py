#!/usr/bin/python3
"""Defines a Student class with serialization and deserialization."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return the dictionary representation of a Student instance.

        If attrs is a list of strings, only attributes in this list
        are returned. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary.

        json is always a dictionary where keys are attribute names and
        values are the new attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
