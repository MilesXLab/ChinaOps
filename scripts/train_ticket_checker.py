#!/usr/bin/env python3
"""
China Train Ticket Verification Helper
Pre-verifies name format, dates, and common issues before booking 12306 tickets

Usage:
    python train_ticket_checker.py --first-name John --last-name Smith --date 2026-02-15 --from BJS --to SHA
    
City Codes:
    BJS = Beijing    |  SHA = Shanghai   |  GZ = Guangzhou   |  CQ = Chongqing
    CDW = Chengdu    |  HGH = Hangzhou   |  XA = Xi'an       |  SH = Shenyang
    
Example:
    python train_ticket_checker.py --first-name John --last-name Smith --date 2026-02-15 --from BJS --to SHA
    
Output:
    Checks name format compatibility, date validity, common issues
"""

import argparse
import sys
from datetime import datetime, timedelta


def validate_name_format(first_name: str, last_name: str) -> dict:
    """
    Validate passport name format for 12306 compatibility
    
    Returns list of issues and recommendations
    """
    
    issues = []
    warnings = []
    
    # Check for special characters
    if not first_name.replace('-', '').replace("'", '').isalpha():
        issues.append("First name contains non-alphabetic characters")
    
    if not last_name.replace('-', '').replace("'", '').isalpha():
        issues.append("Last name contains non-alphabetic characters")
    
    # Check for accents
    import unicodedata
    first_ascii = all(ord(c) < 128 for c in first_name)
    last_ascii = all(ord(c) < 128 for c in last_name)
    
    if not first_ascii or not last_ascii:
        warnings.append("Name contains non-ASCII characters (accents, umlauts). Remove before registration.")
    
    # Check length
    if len(first_name) < 2:
        issues.append("First name too short (minimum 2 characters)")
    if len(last_name) < 2:
        issues.append("Last name too short (minimum 2 characters)")
    
    # Check for compound names
    if ' ' in first_name or ' ' in last_name:
        warnings.append("Name contains spaces. Some systems may split incorrectly. Register as one word in 12306.")
    
    # Format MRZ
    mrz_first = first_name.upper().replace('-', '').replace("'", '')
    mrz_last = last_name.upper().replace('-', '').replace("'", '')
    mrz_format = f"{mrz_last}<<{mrz_first}"
    
    return {
        'issues': issues,
        'warnings': warnings,
        'mrz_format': mrz_format,
        'is_valid': len(issues) == 0
    }


def validate_travel_date(travel_date_str: str) -> dict:
    """
    Validate travel date for ticket booking
    
    12306 allows booking 30 days in advance
    """
    
    issues = []
    warnings = []
    
    try:
        travel_date = datetime.strptime(travel_date_str, '%Y-%m-%d')
    except ValueError:
        return {
            'issues': ["Invalid date format. Use YYYY-MM-DD"],
            'warnings': [],
            'is_valid': False,
            'booking_status': 'INVALID'
        }
    
    today = datetime.now()
    days_until = (travel_date - today).days
    
    # Check if date is in past
    if days_until < 0:
        issues.append(f"Travel date is in the past (was {abs(days_until)} days ago)")
    
    # Check if too far in future
    if days_until > 60:
        warnings.append(f"Travel date is {days_until} days away. Tickets may not be available yet. Check back later.")
    
    # Check if too soon (less than 24 hours)
    if 0 <= days_until < 1:
        issues.append("Travel date is less than 24 hours away. Name verification may fail. Book immediately.")
    
    # Check booking window (optimized is 30 days)
    if 20 <= days_until <= 30:
        booking_status = "✅ OPTIMAL - Book now"
    elif 1 <= days_until < 20:
        booking_status = "✅ GOOD - Available to book"
    elif days_until > 30:
        booking_status = "⏰ NOT YET - Wait to book"
    else:
        booking_status = "⚠️  RISKY - May not work"
    
    return {
        'issues': issues,
        'warnings': warnings,
        'travel_date': travel_date_str,
        'days_until_travel': days_until,
        'booking_status': booking_status,
        'is_valid': len(issues) == 0
    }


def main():
    parser = argparse.ArgumentParser(description='Verify train ticket booking details for 12306')
    parser.add_argument('--first-name', required=True, help='Your first name')
    parser.add_argument('--last-name', required=True, help='Your last name')
    parser.add_argument('--date', required=True, help='Travel date (YYYY-MM-DD)')
    parser.add_argument('--from', dest='from_city', required=False, help='From city code')
    parser.add_argument('--to', dest='to_city', required=False, help='To city code')
    
    args = parser.parse_args()
    
    # Validate name
    name_result = validate_name_format(args.first_name, args.last_name)
    
    # Validate date
    date_result = validate_travel_date(args.date)
    
    # Display results
    print("\n" + "="*70)
    print("🚄 12306 TRAIN TICKET PRE-VERIFICATION CHECKER")
    print("="*70)
    
    # Name section
    print("\n📝 NAME FORMAT CHECK:")
    print("-"*70)
    print(f"First Name:         {args.first_name}")
    print(f"Last Name:          {args.last_name}")
    print(f"MRZ Format:         {name_result['mrz_format']}")
    
    if name_result['is_valid']:
        print("✅ Status:          Name format is VALID for 12306")
    else:
        print("❌ Status:          Name format has ISSUES")
        for issue in name_result['issues']:
            print(f"   ❌ {issue}")
    
    for warning in name_result['warnings']:
        print(f"   ⚠️  {warning}")
    
    # Date section
    print("\n📅 TRAVEL DATE CHECK:")
    print("-"*70)
    print(f"Travel Date:        {date_result['travel_date']}")
    print(f"Days Until Travel:  {date_result['days_until_travel']}")
    print(f"Booking Status:     {date_result['booking_status']}")
    
    if not date_result['is_valid']:
        for issue in date_result['issues']:
            print(f"   ❌ {issue}")
    
    for warning in date_result['warnings']:
        print(f"   ⚠️  {warning}")
    
    # Summary
    print("\n" + "="*70)
    print("📋 VERIFICATION SUMMARY:")
    print("="*70)
    
    if name_result['is_valid'] and date_result['is_valid']:
        print("✅ Ready to book! Your details appear to be correct.")
        print("\n🎫 NEXT STEPS:")
        print("   1. Go to 12306.cn (website or app)")
        print("   2. Register account with MRZ format name:")
        print(f"      {name_result['mrz_format']}")
        print("   3. Complete 24-hour verification window")
        print("   4. Book ticket 24+ hours before travel")
        print("   5. Bring original passport to station")
    else:
        print("⚠️  Please fix the issues above before attempting to book")
    
    print("="*70 + "\n")
    
    # Exit code
    sys.exit(0 if (name_result['is_valid'] and date_result['is_valid']) else 1)


if __name__ == "__main__":
    main()
