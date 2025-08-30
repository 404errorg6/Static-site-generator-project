import unittest
from block_mardown import BlockType, markdown_to_blocks, block_to_block_type

class TestBTBType(unittest.TestCase):
    def test_1(self):
        block = """#### H4 heading text"""     
        typpe = block_to_block_type(block)
        self.assertEqual(typpe, BlockType.HEADING4)

    def test_2(self):
        block = """
        This is a paragraph. Or is it?
        """
        tyype = block_to_block_type(block)
        self.assertEqual(tyype, BlockType.PARAGRAPH)

    def test_3(self):
        block = """```
Time to do some code hehe
```"""
        tyype = block_to_block_type(block)
        self.assertEqual(tyype, BlockType.CODE)

    def test_4(self):
        block = """> Being right doesn't mean anything in this world unless you have the power too
"""
        tyype = block_to_block_type(block)
        self.assertEqual(tyype, BlockType.QUOTE)

    def test_5(self):
        bucket_list = """- Gaming pc(Though won't have time for gaming when actually get it)
- Travel across world
- Be dead rich
- Face fears
- Be respectable
- Be courteous
"""
        tyype = block_to_block_type(bucket_list)
        self.assertEqual(tyype, BlockType.UNORDERED_LIST)

    def test_6(self):
        solution = """1. Open cmd prompt
2. Navigate to C drive
3. Delete system32"""
        tyype = block_to_block_type(solution)
        self.assertEqual(tyype, BlockType.ORDERED_LIST)

    def test_e1(self):
        block = """```
Time to do some code hehe
``
"""
        with self.assertRaises(ValueError):
            block_to_block_type(block)

    def test_e2(self):
        solution = """1. Open cmd prompt
2. Navigate to C drive
5. Delete system32
6. Done
"""
        with self.assertRaises(ValueError):
            block_to_block_type(solution)

class TestMDtoBlock(unittest.TestCase):
    def test_1(self):
        md = """
Hello 


















Far away after several lines
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "Hello",
                    "Far away after several lines"
                    ]
                )
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
