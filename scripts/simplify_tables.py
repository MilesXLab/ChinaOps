import os
import re

def simplify_table_delimiters(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                lines = content.splitlines()
                transformed = False
                new_lines = []
                for line in lines:
                    # Match a typical table separator row like | :--- | ---: | :---: |
                    if re.match(r'^\s*\|\s*[:\-|\s]+\s*\|\s*$', line) and ('---' in line):
                        line = line.replace('---', '-')
                        transformed = True
                    new_lines.append(line)
                
                if transformed:
                    print(f"Simplified table in {file_path}")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write('\n'.join(new_lines))

if __name__ == "__main__":
    simplify_table_delimiters('docs')
