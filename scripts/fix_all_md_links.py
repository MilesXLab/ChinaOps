import os
import re

def fix_md_links(directory):
    # Regex for Markdown links: [label](path.md)
    # We want to change it to [label](path.html)
    # But only for relative paths (not http, etc)
    link_pattern = re.compile(r'\[([^\]]+)\]\(((?!http|https|#)[^)]+)\.md\)')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = link_pattern.sub(r'[\1](\2.html)', content)

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated links in: {file_path}")

if __name__ == "__main__":
    fix_md_links("docs")
    # Also update README.md
    with open("README.md", 'r', encoding='utf-8') as f:
        content = f.read()
    link_pattern = re.compile(r'\[([^\]]+)\]\(((?!http|https|#)[^)]+)\.md\)')
    new_content = link_pattern.sub(r'[\1](\2.html)', content)
    if new_content != content:
        with open("README.md", 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated links in: README.md")
