import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace index/ with just /
content = content.replace('index/', '')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html documentation links cleaned (removed redundant index/)")
