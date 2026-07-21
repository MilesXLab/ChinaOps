import os
import sys
import yaml
from datetime import datetime, timedelta


def check_ttl(directory):
    current_date = datetime.now()
    print(f"--- ChinaOps TTL Audit (System Date: {current_date.strftime('%Y-%m-%d')}) ---")

    expired_count = 0
    total_checked = 0
    missing_count = 0
    skipped_index = 0
    high_churn_count = 0
    high_churn_soon = 0  # <= 7 days remaining

    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith(".md"):
                continue
            # Category hubs / library indexes / maintenance registry are not SOP bodies
            if file.lower() in {
                "index.md",
                "symptom-index.md",
                "high-churn-registry.md",
                "print-pack.md",
                "phrase-style-guide.md",
                "field-retest-checklist.md",
                "field-retest-log.md",
                "design-tokens.md",
                "preflight-checklist.md",
            }:
                skipped_index += 1
                continue

            file_path = os.path.join(root, file)
            total_checked += 1

            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if content.startswith("---"):
                    try:
                        _, frontmatter_text, _ = content.split("---", 2)
                        data = yaml.safe_load(frontmatter_text)

                        if data and "metadata" in data:
                            meta = data["metadata"]
                            last_val = datetime.strptime(str(meta["last_validated"]), "%Y-%m-%d")
                            ttl = int(meta["ttl_days"])
                            expiry_date = last_val + timedelta(days=ttl)
                            days_left = (expiry_date - current_date).days
                            churn = str(meta.get("churn", "")).lower()
                            high = churn == "high" or ttl <= 30
                            if high:
                                high_churn_count += 1

                            if current_date > expiry_date:
                                tag = "EXPIRED-HIGH" if high else "EXPIRED"
                                print(f"[{tag}] {file}: Expired on {expiry_date.strftime('%Y-%m-%d')}")
                                expired_count += 1
                            else:
                                tag = "HIGH" if high else "OK"
                                print(f"[{tag}] {file}: {days_left} days remaining (ttl={ttl})")
                                if high and days_left <= 7:
                                    high_churn_soon += 1
                        else:
                            print(f"[MISSING] {file}: No SRE metadata found")
                            missing_count += 1
                    except Exception as e:
                        print(f"[ERROR] {file}: Failed to parse ({e})")
                        missing_count += 1
                else:
                    print(f"[MISSING] {file}: No frontmatter")
                    missing_count += 1

    print(
        f"\nAudit Summary: {total_checked} SOPs checked, "
        f"{expired_count} expired, {missing_count} missing metadata, "
        f"{high_churn_count} high-churn, {high_churn_soon} high-churn due within 7 days "
        f"(skipped {skipped_index} non-SOP md files)."
    )
    return expired_count + missing_count


if __name__ == "__main__":
    failures = check_ttl("docs")
    sys.exit(1 if failures else 0)
