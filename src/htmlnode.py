class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""
        string = ""
        for key, val in self.props.items():
            string += f' {key}="{val}"'
        return string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        void_elements = ["img", "br", "hr", "input", "link", "meta", "base", "embed", "param", "source", "track", "area", "col"]

        if self.tag not in void_elements and not self.value:
            raise ValueError("value is required for LeafNode")
        if not self.tag:
            return self.value

        if (self.tag == 'a' or self.tag == "img") and not self.props:
            raise ValueError(f'props field is required for "{self.tag}" tag')

        if self.tag == 'a':
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        if self.tag == "img":
            return f'<{self.tag}{self.props_to_html()}/>'
        
        if self.tag in ['i', 'b', 'p', "code", "span", "div", "pre"
                        ]:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        raise TypeError(f'Unknown tag "{self.tag}"')

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("tag is required for ParentNode")
        if not self.children:
            raise ValueError("children is required for ParentNode")
        
        end = ""
        for child in self.children:
            end += child.to_html()

        return f'<{self.tag}>{end}</{self.tag}>'
