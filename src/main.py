import os
from static_gen import copy_content, generate_pages_recursive

def main():
    cd = os.getcwd()
    source = os.path.join(cd, "content/")
    template_path = os.path.join(cd, "template.html")
    dest = os.path.join(cd, "public")

    copy_content("static", "public")
    generate_pages_recursive(source, template_path, dest)
    
main()
