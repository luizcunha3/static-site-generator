import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_rep(self):
        node = TextNode("A text node", TextType.NORMAL, "https://boot.dev/")
        text_rep = node.__repr__()
        self.assertEqual("TextNode(A text node, normal_text, https://boot.dev/)", text_rep)
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq_text_different_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_not_eq_text_type_different_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)
    
    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev/")
        self.assertEqual(node, node2)
    
    def test_not_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://boot.dev/")
        node2 = TextNode("This is a text node", TextType.BOLD, "https://globo.com/")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
    