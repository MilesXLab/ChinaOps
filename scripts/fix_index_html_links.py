import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace .html with / in all href attributes that point to docs/
# Regex: href="(./docs/[^"]+)\.html"
# We exclude things that are actual .html files (like index.html itself)
content = re.sub(r'href="((\./)?docs/[^"]+)\.html"', r'href="\1/"', content)

# Special case for README
content = re.sub(r'href="((\./)?scripts/README)\.md"', r'href="\1.md"', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html documentation links updated to pretty URLs (trailing slash)")
