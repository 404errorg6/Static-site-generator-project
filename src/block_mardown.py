import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING1 = "heading1"
    HEADING2 = "heading2"
    HEADING3 = "heading3"
    HEADING4 = "heading4"
    HEADING5 = "heading5"
    HEADING6 = "heading6"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    def raise_err(tyype):
        raise ValueError(f'Invalid markdown: ({tyype}) does not have matching ending')

    h1, h2, h3, h4, h5, h6 = "# ", "## ", "### ", "#### ", "##### ", "###### "
    code = "```"
    quote = "> "
    uord = "- "

    if block.startswith(code):
        if block.endswith(code):
            return BlockType.CODE
        else:
            raise_err(code)
    
    if block.startswith(quote):
        return BlockType.QUOTE

    if block.startswith(uord):
        return BlockType.UNORDERED_LIST

    if ol_finder(block):
        return BlockType.ORDERED_LIST

    if block.startswith(h1):
        return BlockType.HEADING1
    
    if block.startswith(h2):
        return BlockType.HEADING2

    if block.startswith(h3):
        return BlockType.HEADING3

    if block.startswith(h4):
        return BlockType.HEADING4

    if block.startswith(h5):
        return BlockType.HEADING5

    if block.startswith(h6):
        return BlockType.HEADING6
    
    return BlockType.PARAGRAPH

def ol_finder(block):
    if re.match(r"\d+\. ", block):
        n = int(block.split(". ")[0])
        lines = []
        for line in block.split("\n"):
            if not line:
                continue
            if line.startswith(f"{n}. "):
                lines.append(line.split(f"{n}. ")[1])
                n += 1
            else:
                raise ValueError(f'Invalid markdown ordered_list: ({line.split(".")[0]}) does not match leading line sequence')
        return lines

def markdown_to_blocks(markdown):
    output = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if not block:
            continue
        block = block.strip()
        output.append(block)
    return output
       

