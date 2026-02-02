import os
import re

def check_links(file_path):
    print(f"Checking links in: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    is_html = file_path.endswith('.html')
    if is_html:
        links = re.findall(r'href="([^"]+)"', content)
    else:
        links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)

    base_dir = os.path.dirname(file_path)
    failures = []

    for link in links:
        if link.startswith(('http', 'mailto:', '#', 'javascript:')):
            continue
        
        clean_link = link.split('?')[0].split('#')[0]
        if not clean_link: continue

        target = os.path.normpath(os.path.join(base_dir, clean_link))
        
        if not os.path.exists(target):
            # Check if it's a directory link (trailing slash) which Jekyll converts from .md
            if link.endswith('/'):
                # Try target + ".md" (if it's a file in same dir)
                # or target + "/index.md" (if it's a subdirectory)
                md_file = target + ".md"
                index_file = os.path.join(target, "index.md")
                if os.path.exists(md_file) or os.path.exists(index_file):
                    continue
            
            # Special case for .html links in the verify script (for hosted testing)
            if target.endswith('.html'):
                md_target = target[:-5] + '.md'
                if os.path.exists(md_target):
                    continue

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
        print("\nAll links verified (Trailing Slash / Jekyll pattern)!")
