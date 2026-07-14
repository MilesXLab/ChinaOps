#!/usr/bin/env python3
"""
China Digital Entry Formatter
Formats and validates information for the China Digital Arrival Card (Alipay/WeChat)
to prevent formatting errors, character issues, and border kiosk validation rejections.

Usage:
    python scripts/digital_entry_formatter.py
"""

import sys
import re
from datetime import datetime
import unicodedata

def clean_and_uppercase(text: str) -> str:
    """Normalize accents, remove special characters, and uppercase"""
    if not text:
        return ""
    nfd = unicodedata.normalize('NFD', text.strip())
    cleaned = ''.join(char for char in nfd if unicodedata.category(char) != 'Mn')
    # Keep only alphanumeric characters and spaces
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned)
    return cleaned.upper()

def validate_date(date_str: str) -> str:
    """Validate and format birth/expiration dates as YYYY-MM-DD"""
    date_str = date_str.strip()
    # Try different separators
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y", "%Y%m%d"):
        try:
            dt = datetime.strptime(date_str.replace('/', '-'), fmt.replace('/', '-'))
            return dt.strftime("%Y-%m-%d")
        except ValueError:
            continue
    raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def validate_flight(flight_str: str) -> str:
    """Validate flight number format (e.g., MU588, CX368, AA123)"""
    flight = flight_str.strip().upper().replace(" ", "")
    if not re.match(r'^[A-Z0-9]{2,3}\d{3,4}$', flight):
        print("⚠️  Warning: Flight number format looks atypical (should be e.g., MU588, UA857).")
    return flight

def validate_phone(phone_str: str) -> str:
    """Validate contact number format"""
    phone = phone_str.strip().replace(" ", "").replace("-", "")
    if not phone.startswith("+") and len(phone) > 10:
        print("💡 Tip: Consider prefixing phone numbers with a country code (e.g. +1, +44).")
    return phone

def run_interactive():
    print("\n" + "="*60)
    print("📋 CHINA DIGITAL ENTRY FORMATTER (v1.3)")
    print("="*60)
    print("This script validates and formats details required for China's")
    print("Digital Arrival Card (filled out in Alipay/WeChat before landing).")
    print("="*60 + "\n")

    try:
        # 1. Names
        family_name = input("1. Family Name / Surname (as in passport): ")
        while not family_name.strip():
            family_name = input("❌ Family Name is required: ")
        
        given_names = input("2. Given Name / First & Middle Names (as in passport): ")
        while not given_names.strip():
            given_names = input("❌ Given Name is required: ")

        # 2. Gender
        gender = input("3. Gender (M/F): ").strip().upper()
        while gender not in ('M', 'F'):
            gender = input("❌ Invalid input. Please enter 'M' or 'F': ").strip().upper()
        gender_full = "MALE (男)" if gender == 'M' else "FEMALE (女)"

        # 3. Date of Birth
        dob_input = input("4. Date of Birth (YYYY-MM-DD): ")
        while True:
            try:
                dob = validate_date(dob_input)
                break
            except ValueError as e:
                dob_input = input(f"❌ {e} Re-enter Date of Birth (YYYY-MM-DD): ")

        # 4. Nationality
        nationality = input("5. Nationality (e.g., UNITED KINGDOM, CANADA, USA): ")
        while not nationality.strip():
            nationality = input("❌ Nationality is required: ")

        # 5. Passport Number
        passport_num = input("6. Passport Number: ")
        while not passport_num.strip():
            passport_num = input("❌ Passport Number is required: ")

        # 6. Visa Status
        print("\nVisa Status Options:")
        print("  [1] 30-Day Visa-Free (Pilot Scheme - UK, Canada, Germany, Australia, etc.)")
        print("  [2] Transit Visa-Free (144-Hour / 240-Hour TWOV)")
        print("  [3] Tourist Visa (L-Visa)")
        print("  [4] Other")
        visa_opt = input("7. Select Visa Option (1-4): ").strip()
        while visa_opt not in ('1', '2', '3', '4'):
            visa_opt = input("❌ Please select a number between 1 and 4: ").strip()
        
        if visa_opt == '1':
            visa_type = "VISA-FREE (30-DAY PILOT)"
        elif visa_opt == '2':
            visa_type = "TRANSIT VISA-FREE (144/240-HOUR TWOV)"
        elif visa_opt == '3':
            visa_type = "TOURIST VISA (L-VISA)"
        else:
            visa_type = input("Enter custom Visa status: ").strip().upper()

        # 7. Flight / Vessel / Train Number
        flight_input = input("8. Inbound Flight/Train Number (e.g., MU588): ")
        while not flight_input.strip():
            flight_input = input("❌ Inbound Flight/Train is required: ")
        flight_num = validate_flight(flight_input)

        # 8. Destination Address / Hotel
        hotel_name = input("9. Hotel Name & Address in China (e.g., Westin Bund, Huangpu District, Shanghai): ")
        while not hotel_name.strip():
            hotel_name = input("❌ Address is required: ")

        # 9. Phone Number
        phone_input = input("10. Contact Phone Number (include country code, e.g., +1234567890): ")
        while not phone_input.strip():
            phone_input = input("❌ Phone number is required: ")
        phone_num = validate_phone(phone_input)

        # Output report
        formatted_family = clean_and_uppercase(family_name)
        formatted_given = clean_and_uppercase(given_names)
        formatted_nationality = clean_and_uppercase(nationality)
        formatted_passport = clean_and_uppercase(passport_num)
        formatted_hotel = clean_and_uppercase(hotel_name)

        print("\n" + "="*60)
        print("📊 FORMATTED DIGITAL ARRIVAL CARD DATA")
        print("="*60)
        print("Use the exact string values below to fill out your form:")
        print("-"*60)
        print(f"Family Name:         {formatted_family}")
        print(f"Given Name:          {formatted_given}")
        print(f"Gender:              {gender_full}")
        print(f"Date of Birth:       {dob}")
        print(f"Nationality:         {formatted_nationality}")
        print(f"Passport Number:     {formatted_passport}")
        print(f"Visa Type:           {visa_type}")
        print(f"Flight/Train:        {flight_num}")
        print(f"Address in China:    {formatted_hotel}")
        print(f"Phone Number:        {phone_num}")
        print("="*60)
        print("\n💡 DIGITAL ARRIVAL CARD SOP:")
        print("   1. Open Alipay or WeChat and search for 'Digital Entry Card'.")
        print("   2. Copy-paste these formatted values into the respective fields.")
        print("   3. Ensure you generate a QR code at the end of the entry portal.")
        print("   4. SCREENSHOT the QR code immediately.")
        print("   5. Bring a pen! If kiosks fail or lines are too long at the border,")
        print("      use these exact values to fill out the legacy paper card.")
        print("="*60 + "\n")

    except KeyboardInterrupt:
        print("\n\n❌ Formatting cancelled by user.")
        sys.exit(1)

if __name__ == "__main__":
    run_interactive()
