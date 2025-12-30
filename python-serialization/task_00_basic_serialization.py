#!/usr/bin/env python3
"""Basic serialization module for JSON."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Output JSON filename.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): Input JSON filename.

    Returns:
        dict: Deserialized Python dictionary.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
