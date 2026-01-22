#!/usr/bin/env python3
"""
Passport MRZ Code Converter for 12306 Train Ticket Registration
Converts passport MRZ (Machine Readable Zone) to the format required by 12306

Usage:
    python passport_mrz_converter.py <first_name> <last_name>
    
Example:
    python passport_mrz_converter.py John Smith
    
Output:
    MRZ Format: SMITH<<JOHN
    Copy this into 12306 account registration
"""

import sys


def format_mrz_name(first_name: str, last_name: str) -> str:
    """
    Format passport name into 12306 MRZ format
    
    12306 expects: LASTNAME<<FIRSTNAME
    - All uppercase
    - Spaces replaced with <<
    - No special characters
    - ASCII only (remove accents)
    """
    
    # Remove accents and special characters
    import unicodedata
    
    def remove_accents(text):
        nfd = unicodedata.normalize('NFD', text)
        return ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')
    
    # Clean inputs
    first = remove_accents(first_name.strip()).upper()
    last = remove_accents(last_name.strip()).upper()
    
    # Remove hyphens and apostrophes
    first = first.replace('-', '').replace("'", '')
    last = last.replace('-', '').replace("'", '')
    
    # Format: LASTNAME<<FIRSTNAME
    mrz = f"{last}<<{first}"
    
    return mrz


def main():
    if len(sys.argv) < 3:
        print("❌ Usage: python passport_mrz_converter.py <first_name> <last_name>")
        print("Example: python passport_mrz_converter.py John Smith")
        sys.exit(1)
    
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    
    mrz_format = format_mrz_name(first_name, last_name)
    
    print("\n" + "="*60)
    print("📋 PASSPORT MRZ FORMATTER FOR 12306")
    print("="*60)
    print(f"Input Name:        {first_name} {last_name}")
    print(f"MRZ Format:        {mrz_format}")
    print("="*60)
    print("\n✅ COPY THIS INTO 12306 ACCOUNT:")
    print(f"   {mrz_format}")
    print("\n📌 TIPS:")
    print("   1. Paste this format into 12306 name field")
    print("   2. Verify in 12306 system 24 hours before travel")
    print("   3. Bring original passport to station for verification")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
