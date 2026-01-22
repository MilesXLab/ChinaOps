#!/usr/bin/env python3
"""
Chinese Medication Dose Calculator for Children
Calculates appropriate medication dosage based on child's weight

Usage:
    python child_medication_calculator.py --name "Paracetamol" --weight 20 --dosage-per-kg 15
    
Common Medications:
    - Paracetamol/Acetaminophen: 15 mg/kg per dose
    - Ibuprofen: 10 mg/kg per dose
    - Amoxicillin: 25 mg/kg per dose
    
Example:
    python child_medication_calculator.py --name "Ibuprofen" --weight 25 --dosage-per-kg 10
    Output: For 25kg child, dose is 250mg
"""

import argparse
import sys


def calculate_dose(weight_kg: float, dosage_per_kg: float, max_dose: float = None) -> dict:
    """
    Calculate medication dose based on child's weight
    
    Args:
        weight_kg: Child's weight in kilograms
        dosage_per_kg: Medication dosage per kg (in mg)
        max_dose: Maximum allowed single dose (optional cap)
    
    Returns:
        Dictionary with dosage information
    """
    
    calculated_dose = weight_kg * dosage_per_kg
    
    # Apply max dose cap if specified
    if max_dose and calculated_dose > max_dose:
        calculated_dose = max_dose
        is_capped = True
    else:
        is_capped = False
    
    return {
        'weight_kg': weight_kg,
        'dosage_per_kg': dosage_per_kg,
        'calculated_dose_mg': calculated_dose,
        'is_capped': is_capped
    }


def format_output(medication_name: str, result: dict) -> str:
    """Format the calculation result for display"""
    
    output = f"\n{'='*60}\n"
    output += f"💊 CHILD MEDICATION DOSE CALCULATOR\n"
    output += f"{'='*60}\n"
    output += f"Medication:         {medication_name}\n"
    output += f"Child's Weight:     {result['weight_kg']} kg\n"
    output += f"Dosage per kg:      {result['dosage_per_kg']} mg/kg\n"
    output += f"Calculated Dose:    {result['calculated_dose_mg']:.1f} mg\n"
    
    if result['is_capped']:
        output += f"⚠️  (Capped at maximum dose)\n"
    
    output += f"{'='*60}\n"
    output += f"\n🩺 ADMINISTRATION TIPS:\n"
    output += f"   • Typical dosing: Every 6-8 hours (3-4 times/day)\n"
    output += f"   • Maximum daily: Calculate {result['calculated_dose_mg']:.1f}mg × 4 doses\n"
    output += f"   • Do NOT exceed maximum daily dose without doctor approval\n"
    output += f"   • Give with food to reduce stomach upset\n"
    output += f"\n⚠️  IMPORTANT:\n"
    output += f"   • This is for REFERENCE ONLY\n"
    output += f"   • Always consult pediatrician before administering\n"
    output += f"   • Show calculation to pharmacist for verification\n"
    output += f"{'='*60}\n"
    
    return output


def main():
    parser = argparse.ArgumentParser(
        description='Calculate medication dosage for children based on weight'
    )
    parser.add_argument('--name', required=True, help='Medication name')
    parser.add_argument('--weight', type=float, required=True, help='Child weight in kg')
    parser.add_argument('--dosage-per-kg', type=float, required=True, help='Dosage per kg (mg/kg)')
    parser.add_argument('--max-dose', type=float, default=None, help='Maximum single dose cap (optional)')
    
    args = parser.parse_args()
    
    # Validate inputs
    if args.weight <= 0 or args.dosage_per_kg <= 0:
        print("❌ Error: Weight and dosage must be positive numbers")
        sys.exit(1)
    
    if args.weight > 100:
        print("⚠️  Warning: Weight seems unusually high. Verify input.")
    
    # Calculate
    result = calculate_dose(args.weight, args.dosage_per_kg, args.max_dose)
    
    # Display
    output = format_output(args.name, result)
    print(output)


if __name__ == "__main__":
    main()
