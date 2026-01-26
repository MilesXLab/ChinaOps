import os
import yaml
from datetime import datetime, timedelta

def check_ttl(directory):
    current_date = datetime.now()
    print(f"--- ChinaOps TTL Audit (System Date: {current_date.strftime('%Y-%m-%d')}) ---")
    
    expired_count = 0
    total_checked = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                total_checked += 1
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content.startswith("---"):
                        try:
                            # Extract frontmatter
                            _, frontmatter_text, _ = content.split("---", 2)
                            data = yaml.safe_load(frontmatter_text)
                            
                            if data and 'metadata' in data:
                                meta = data['metadata']
                                last_val = datetime.strptime(str(meta['last_validated']), '%Y-%m-%d')
                                ttl = int(meta['ttl_days'])
                                expiry_date = last_val + timedelta(days=ttl)
                                
                                if current_date > expiry_date:
                                    print(f"[EXPIRED] {file}: Expired on {expiry_date.strftime('%Y-%m-%d')}")
                                    expired_count += 1
                                else:
                                    days_left = (expiry_date - current_date).days
                                    print(f"[OK] {file}: {days_left} days remaining")
                            else:
                                print(f"[MISSING] {file}: No SRE metadata found")
                        except Exception as e:
                            print(f"[ERROR] {file}: Failed to parse ({e})")

    print(f"\nAudit Summary: {total_checked} files checked, {expired_count} expired.")
    return expired_count

if __name__ == "__main__":
    # Check the docs directory
    check_ttl("docs")
