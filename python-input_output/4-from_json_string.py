#!/usr/bin/python3
"""Returns an object (Python data structure) from a JSON string."""

import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    return json.loads(my_str)
