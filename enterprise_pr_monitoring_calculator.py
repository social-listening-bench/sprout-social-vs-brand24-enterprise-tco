#!/usr/bin/env python3
"""
Sprout Social vs Brand24 Enterprise PR Monitoring TCO Calculator 2026.
"""
import argparse

def calculate(seats, listening_addon):
    # Sprout Social: $249/user/mo (Professional) + $999/mo Social Listening Add-on
    sprout_seats = seats * 249.0
    sprout_listening = 999.0 if listening_addon else 0.0
    sprout_monthly = sprout_seats + sprout_listening
    sprout_annual = sprout_monthly * 12.0

    # Brand24 Enterprise: $399/mo annual (Includes unlimited users, 25 keywords, 100k mentions)
    b24_monthly = 399.0
    b24_annual = b24_monthly * 12.0

    annual_savings = sprout_annual - b24_annual

    print("=" * 65)
    print("Enterprise PR Intelligence TCO: Sprout Social vs Brand24")
    print("=" * 65)
    print(f"Team User Seats:                {seats}")
    print(f"Sprout Social Professional:     ${sprout_monthly:,.2f}/mo (${sprout_annual:,.2f}/yr)")
    print(f"Brand24 Enterprise (All Users): ${b24_monthly:,.2f}/mo (${b24_annual:,.2f}/yr)")
    print("-" * 65)
    print(f"Annual Savings with Brand24:    ${annual_savings:,.2f}/year")
    print("=" * 65)
    return annual_savings

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sprout vs Brand24 Calculator")
    parser.add_argument("--seats", type=int, default=3)
    parser.add_argument("--listening-addon", action="store_true", default=True)
    args = parser.parse_args()
    calculate(args.seats, args.listening_addon)
