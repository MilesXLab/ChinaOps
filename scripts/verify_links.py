import os
import re

def check_links(file_path):
    print(f"Checking links in: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all href="..." or [...] (...)
    is_html = file_path.endswith('.html')
    if is_html:
        links = re.findall(r'href="([^"]+)"', content)
    else:
        # Markdown links: [label](path)
        links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)

    base_dir = os.path.dirname(file_path)
    failures = []

    for link in links:
        if link.startswith(('http', 'mailto:', '#', 'javascript:')):
            continue
        
        # Clean query or hash
        clean_link = link.split('?')[0].split('#')[0]
        if not clean_link:
            continue

        # Target path
        target = os.path.normpath(os.path.join(base_dir, clean_link))
        
        # Check existence
        if not os.path.exists(target):
            # Try with .md if it's a directory link and missing
            if not os.path.isdir(target) and not target.endswith('.md'):
                if os.path.exists(target + '.md'):
                    failures.append(f"MISSING .md extension: {link} -> {target}")
                    continue
            
            # Special case for directories with index.md
            if os.path.isdir(target):
                if not os.path.exists(os.path.join(target, 'index.md')):
                    failures.append(f"DIR MISSING index.md: {link} -> {target}")
            else:
                failures.append(f"BROKEN: {link} -> {target}")
    
    return failures

if __name__ == "__main__":
    all_failures = {}
    files_to_check = ['index.html', 'README.md']
    for root, dirs, files in os.walk('docs'):
        for file in files:
            if file.endswith('.md'):
                files_to_check.append(os.path.join(root, file))

    for f in files_to_check:
        res = check_links(f)
        if res:
            all_failures[f] = res

    if all_failures:
        print("\n=== LINK FAILURES FOUND ===\n")
        for f, fails in all_failures.items():
            print(f"{f}:")
            for fail in fails:
                print(f"  - {fail}")
    else:
        print("\nAll links verified!")
