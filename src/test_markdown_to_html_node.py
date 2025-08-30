import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMDtoHTMLnode(unittest.TestCase):
    def test_mini(self):
        md = """
1. check1
2. check2
3. check3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                '<div><ol><li>check1</li><li>check2</li><li>check3</li></ol></div>'
                )
    def test_1(self):
        self.maxDiff = None
        md = """
## **Bolded Heading2**

> _With great powers come great responsibilities_

![uncle ben](https://spiderman.com)

Press this [Linker](https://rickroll.com)
same block man

```
sudo rm -rf /*
```

- Element check1
- Element check2
- Element check3

1. First item
2. Second item
3. Third item



The end
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                """<div><h2><b>Bolded Heading2</b></h2><blockquote><i>With great powers come great responsibilities</i></blockquote><p><img src="https://spiderman.com" alt="uncle ben"/></p><p>Press this <a href="https://rickroll.com">Linker</a> same block man</p><pre><code>sudo rm -rf /*\n</code></pre><ul><li>Element check1</li><li>Element check2</li><li>Element check3</li></ul><ol><li>First item</li><li>Second item</li><li>Third item</li></ol><p>The end</p></div>"""
                )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
