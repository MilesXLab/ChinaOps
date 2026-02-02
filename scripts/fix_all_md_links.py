import os
import re

def fix_all_links_to_pretty(directory):
    # Match [label](path.html) or [label](path)
    # We want to change it to [label](path/)
    # But only for relative paths (not http, mailto, etc)
    # And we exclude index.html
    
    # Regex: [label](rel_path)
    link_pattern = re.compile(r'\[([^\]]+)\]\(((?!http|https|#|mailto:)[^)]+)\)')

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                def replace_link(match):
                    label = match.group(1)
                    path = match.group(2)
                    
                    # Clean up existing extensions if they were added
                    if path.endswith('.md'):
                        path = path[:-3]
                    elif path.endswith('.html'):
                        path = path[:-5]
                    
                    # Ensure trailing slash
                    if not path.endswith('/'):
                        path += '/'
                    
                    return f'[{label}]({path})'

                new_content = link_pattern.sub(replace_link, content)

                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated links in: {file_path}")

if __name__ == "__main__":
    fix_all_links_to_pretty("docs")
    # Also update README.md
    file_path = "README.md"
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    link_pattern = re.compile(r'\[([^\]]+)\]\(((?!http|https|#|mailto:)[^)]+)\)')
    def replace_link(match):
        label = match.group(1)
        path = match.group(2)
        if path.endswith('.md'): path = path[:-3]
        elif path.endswith('.html'): path = path[:-5]
        if not path.endswith('/'): path += '/'
        return f'[{label}]({path})'
    
    new_content = link_pattern.sub(replace_link, content)
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in: {file_path}")
