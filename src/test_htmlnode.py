import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        props = {
            "style": "background-color:red"
        }
        props_str = f' style="background-color:red"'
        node = HTMLNode("h1", "Hello", None, props)

        self.assertEqual(node.props_to_html(), props_str)

    def test_props_none(self):
            node = HTMLNode("h1", "Hello", None, None)
    
            self.assertEqual(node.props_to_html(), '')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        props = {
             "style": "background-color:red"
        }
        node = LeafNode("h1", "Hello, world!", props)
        self.assertEqual(node.to_html(), "<h1 style=\"background-color:red\">Hello, world!</h1>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_parent_nodes(self):
        grandchild_node1 = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("h2", "bro")
        child_node1 = ParentNode("span", [grandchild_node1])
        child_node2 = ParentNode("div", [grandchild_node2])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><div><h2>bro</h2></div></div>",
        )

if __name__ == "__main__":
    unittest.main()