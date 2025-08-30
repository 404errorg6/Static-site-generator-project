from block_mardown import markdown_to_blocks, block_to_block_type, BlockType, ol_finder
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextType, TextNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

def markdown_to_html_node(markdown):
    final_node = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            text = block.split("```", 2)[1]
            text = text.removeprefix("\n")
            text_node = TextNode(text, TextType.CODE)
            html_node = text_node_to_html_node(text_node)
            final_node.append(ParentNode("pre", children=[html_node]))
        else:
            node = block_type_to_html_node(block, block_type)
            final_node.append(node)
    parent = ParentNode("div", children=final_node)
    return parent
        

def block_type_to_html_node(block, block_type):
    if block_type == BlockType.PARAGRAPH:
        
        child_nodes = text_to_children(block.removeprefix("\n").removesuffix("\n"))
        return ParentNode("p", children=child_nodes)

    if block_type == BlockType.QUOTE:
        print(f"block -----> {block}")
        quotes = block.split("\n")
        child_nodes = []
        for quote in quotes:
            text = quote.strip("> ")
            if text:
                child_nodes.extend(text_to_children(text))

        return ParentNode("blockquote", children=child_nodes)

    if block_type == BlockType.ORDERED_LIST:
        children =  ol_to_children(block)
        return ParentNode("ol", children=children)

    if block_type == BlockType.UNORDERED_LIST:
        children = ul_to_children(block)
        return ParentNode("ul", children=children)

    if block_type == BlockType.HEADING1:
        heading = stripper(block, "# ")
        child_nodes = text_to_children(heading)
        return ParentNode("h1", children=child_nodes)

    if block_type == BlockType.HEADING2:
        heading = stripper(block, "## ")
        child_nodes = text_to_children(heading)
        return ParentNode("h2", children=child_nodes)

    if block_type == BlockType.HEADING3:
        heading = stripper(block, "### ")
        child_nodes = text_to_children(heading)
        return ParentNode("h3", children=child_nodes)

    if block_type == BlockType.HEADING4:
        heading = stripper(block, "#### ")
        child_nodes = text_to_children(heading)
        return ParentNode("h4", children=child_nodes)

    if block_type == BlockType.HEADING5:
        heading = stripper(block, "##### ")
        child_nodes = text_to_children(heading)
        return ParentNode("h5", children=child_nodes)

    if block_type == BlockType.HEADING6:
        heading = stripper(block, "###### ")
        child_nodes = text_to_children(heading)
        return ParentNode("h6", children=child_nodes)

def text_to_children(text):
    children = []
    text = text.replace("\n", " ")
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def stripper(block, ID):
    return block.split(ID)[1]

def ol_to_children(block):
    children = []
    lines = ol_finder(block)
    for line in lines:
        child_nodes = text_to_children(line)
        children.append(ParentNode("li", children=child_nodes))
    return children

def ul_to_children(block):
    children = []
    lines = []
    for line in block.split("\n"):
        if not line:
            continue
        if line.startswith("- "):
            line = line.split("- ", 1)[1]
            child_nodes = text_to_children(line)
            lines.append(child_nodes)
        else:
            raise ValueError('Invalid markdown unordered_list: Line does not start with "-".')
    for line in lines:
        children.append(ParentNode("li", children=line))
    return children
