#!/usr/bin/env python3
"""Custom object serialization and deserialization using pickle."""

import pickle


class CustomObject:
    """CustomObject class for demonstrating pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.

        Returns None if serialization fails.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a file using pickle.

        Returns None if deserialization fails.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
