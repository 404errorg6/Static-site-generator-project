import os
import sys
from static_gen import copy_content, generate_pages_recursive

def input_handler():
    base_path = sys.argv[1]
    if not base_path:
        base_path = "/"
    return base_path

def main():
    base_path = input_handler()
    cd = os.getcwd()
    source = os.path.join(cd, "content")
    template_path = os.path.join(cd, "template.html")
    dest = os.path.join(cd, "docs")

    copy_content("static", "docs")
    generate_pages_recursive(source, template_path, dest, base_path)
    
main()
