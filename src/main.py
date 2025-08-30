import os
from static_gen import copy_content, generate_page

def main():
    cd = os.getcwd()
    source = os.path.join(cd, "content/index.md")
    template_path = os.path.join(cd, "template.html")
    dest = os.path.join(cd, "public")
    copy_content("static", "public")
    generate_page(source, template_path, dest)

main()
