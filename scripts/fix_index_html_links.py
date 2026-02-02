import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .md with .html in all href attributes that point to docs/
# Regex: href="(./docs/[^"]+)\.md"
content = re.sub(r'href="((\./)?docs/[^"]+)\.md"', r'href="\1.html"', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html documentation links updated to .html")
