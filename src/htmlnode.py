class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        string = []
        for node in self.props:
            string.append(f"{node}=\"{self.props[node]}\"")
        return " ".join(string)
    
    def __repr__(self):
        return f"| Tag: {self.tag} | Value: {self.value} | Children: {self.children} | Props: {self.props_to_html()}"