#!/usr/bin/env python3
import sys
import markdown
import xml.etree.ElementTree as ET
from xml.dom import minidom

"""
import xml.etree.ElementTree as ET
tree = ET.parse('toc.xml')
root = tree.getroot()
"""
def tokens_to_xml(tokens, parent_element):
    """
    Recursively convert TOC tokens to XML elements.

    Args:
        tokens: List of TOC token dictionaries
        parent_element: Parent XML element to append to
    """
    for t in tokens:
        # Create a section element
        section = ET.SubElement(parent_element, "section")
        section.set("id", t.get("id", ""))
        section.set("level", str(t.get("level", "")))

        # Add the title as a child element
        title = ET.SubElement(section, "title")
        title.text = t["name"]

        # Recursively add children
        if t.get("children"):
            children_elem = ET.SubElement(section, "subsections")
            tokens_to_xml(t["children"], children_elem)


def prettify_xml(elem):
    """
    Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, encoding='unicode')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} path/to/file.md", file=sys.stderr)
        sys.exit(1)

    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        text = f.read()

    md = markdown.Markdown(extensions=["toc"])
    md.convert(text)  # populates md.toc and md.toc_tokens

    tokens = getattr(md, "toc_tokens", None)
    if tokens:
        # Create root element
        root = ET.Element("table_of_contents")
        root.set("source", path)

        # Convert tokens to XML
        tokens_to_xml(tokens, root)

        # Pretty print the XML
        xml_string = prettify_xml(root)
        print(xml_string)
    else:
        print("Error: Could not extract TOC tokens", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
