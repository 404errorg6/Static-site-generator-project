# Static Site Generator

This project is a static site generator that converts Markdown content into a fully functional HTML website using a predefined HTML template. It is designed to be simple, efficient, and customizable.

## Features
- Converts Markdown files to HTML.
- Supports recursive directory structures for organizing content.
- Customizable HTML templates.
- Copies static assets (CSS, images, etc.) to the output directory.

## Project Structure
- `content/`: Contains the Markdown files to be converted.
- `docs/`: The output directory for the generated HTML files.
- `src/`: Source code for the static site generator.
- `static/`: Static assets (e.g., CSS, images) to be copied to the output directory.
- `template.html`: The HTML template used for generating pages.

## How It Works
1. **Markdown Conversion**: Markdown files in the `content/` directory are converted to HTML using the `markdown_to_html_node` module.
2. **Template Integration**: The content is injected into the `template.html` file, replacing placeholders like `{{ Title }}` and `{{ Content }}`.
3. **Static Asset Copying**: Files in the `static/` directory are copied to the `docs/` directory.
4. **Recursive Processing**: Subdirectories in `content/` are processed recursively, maintaining the directory structure in the output.

## Usage
1. Place your Markdown files in the `content/` directory.
2. Customize the `template.html` file as needed.
3. Run the generator:
   ```bash
   python src/main.py
   ```
4. The generated site will be available in the `docs/` directory.

## Requirements
- Python 3.6 or higher.

## Example
Given the following `content/` structure:
```
content/
├── index.md
├── blog/
│   ├── post1/
│   │   └── index.md
│   └── post2/
│       └── index.md
```
The generator will produce:
```
docs/
├── index.html
├── blog/
│   ├── post1/
│   │   └── index.html
│   └── post2/
│       └── index.html
```
