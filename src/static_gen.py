import os
import shutil
from markdown_to_html_node import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from "{from_path}" to "{dest_path}"')
    if not os.path.isfile(from_path):
        raise Exception(f'"{from_path}" is not a file')

    with open(from_path, "r") as file:
        md = file.read()
    with open(template_path, "r") as tmp:
        template = tmp.read()

    html_nodes = markdown_to_html_node(md)
    content = html_nodes.to_html()
    title = extract_title(md)
    
    final = template.replace("{{ Title }}", "AHHHH")
    final = template.replace("{{ Content }}", content)
    
    if not os.path.isdir(dest_path):
        os.makedirs(dest_path, exist_ok=True)
    
    with open(os.path.join(dest_path, "index.html"), "w") as file:
        file.write(final)

def extract_title(markdown):
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):  # H1 header
            return line.strip("# ").strip()
    raise Exception("h1 header not found")

def copy_content(source, destination, so_far=""):
    if not source.startswith("/"):
        source = os.path.join(os.getcwd(), source)
    if not destination.startswith("/"):
        destination = os.path.join(os.getcwd(), destination)
    
    bsource = os.path.basename(source)
    bdest = os.path.basename(destination)

    if not os.path.exists(source) or os.path.isfile(source):
        raise Exception(f'"{bsource}" directory not found')
    if not os.path.exists(destination) or os.path.isfile(destination):
        raise Exception(f'"{bdest}" directory not found')
    
    if not del_dir_contents(destination):
        raise Exception(f'error while deleting "{bdest}"')
    #print(f'Successfully deleted "{bdest}"')

    if not rcopy(source, destination):
        raise Exception(f'error while copying files from "{bsource}" to "{bdest}"')
    print(f'Successfully copied contents from "{bsource}" to "{bdest}"')

def del_dir_contents(dir):
    for content in os.listdir(dir):
        content = os.path.join(dir, os.path.basename(content))
        if os.path.isfile(content):
            os.remove(content)
        if os.path.isdir(content):
            shutil.rmtree(content)
    return 1

def rcopy(source, destination):
    for content in os.listdir(source):
        content = os.path.join(source, content)
        if os.path.isfile(content):
            #print(f'"{os.path.basename(content)}" is file and copied!')
            shutil.copy(content, destination)

        elif os.path.isdir(content):
            new_dir = os.path.join(destination, os.path.basename(content))
            os.mkdir(new_dir)
            rcopy(os.path.join(source, content), new_dir)
    return 1


