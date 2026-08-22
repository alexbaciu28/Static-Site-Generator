class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        attributes = ""
        if self.props == None or len(self.props) == 0:
            return ""
        for attribute, value in self.props.items():
            attributes += f' {attribute}="{value}"'

        return attributes

    def __repr__(self):
        return f" HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("value of leaf node is missing")

        if self.tag == None:
            return self.value

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f" HTMLNode({self.tag}, {self.value}, {self.props_to_html()})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("tag of parent node is missing")

        if self.children == None:
            raise ValueError("children of parent node are missing")

        start = f'<{self.tag}{self.props_to_html()}>'
        middle = ""
        for child in self.children:
            middle += child.to_html()
        end = f'</{self.tag}>'

        return start + middle + end
