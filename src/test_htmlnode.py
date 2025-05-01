import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        html_node = HTMLNode(props={"a": 1, "b": 2})
        html_node_props = html_node.props_to_html()
        self.assertEqual(html_node_props, "a=\"1\" b=\"2\"")
