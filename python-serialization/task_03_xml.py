#!/usr/bin/env python3
"""Serialization and deserialization using XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Python dictionary to serialize.
        filename (str): Output XML filename.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): Input XML filename.

    Returns:
        dict: Deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for element in root:
        result[element.tag] = element.text

    return result
