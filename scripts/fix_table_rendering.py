import os
import re

def fix_table_spacing(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Regex to find lines starting with | that are NOT preceded by a blank line
                # It looks for a non-blank line ([^\n]+) followed by a line starting with |
                # But we must be careful not to match the start of the file or lines that are already part of a table.
                
                # A more robust way: Find all lines starting with |
                # Check the line before it.
                lines = content.splitlines()
                new_lines = []
                for i in range(len(lines)):
                    if lines[i].strip().startswith('|') and i > 0:
                        # Check if previous line is blank or also starts with |
                        prev_line = lines[i-1].strip()
                        if prev_line and not prev_line.startswith('|') and not prev_line.startswith('---'):
                            new_lines.append('')
                    new_lines.append(lines[i])
                
                new_content = '\n'.join(new_lines)
                
                if content != new_content:
                    print(f"Fixing tables in {file_path}")
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)

if __name__ == "__main__":
    fix_table_spacing('docs')
    fix_table_spacing('.') # Also check README.md etc
