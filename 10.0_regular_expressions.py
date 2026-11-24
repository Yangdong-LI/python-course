"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In:
# A campaign ID, an advertising platform and a budget in euros.

# 2. Process:
# Check each field with re.fullmatch().
# Display a specific message for each invalid field.
# Ask for the three fields again if any field is invalid.
# Save the record only when all three fields are acceptable.

# 3. Out:
# A record saved to campaigns.csv.
# Columns: campaign_id, platform, budget_euros.

# 4. My three fields and their rules:
# Campaign ID: uppercase CMP- followed by exactly three ASCII digits.
# Platform: exactly Google, Meta or TikTok, including capitalisation.
# Budget: one to five ASCII digits representing whole euros.
# Zero and leading zeros are accepted.
# Negative numbers, decimals and currency symbols are rejected.
# Surrounding whitespace is removed before validation.
# For example, CMP-000 and budget 00050 are acceptable.
# The budget 00050 is saved as the integer 50.


import re
import csv
from pathlib import Path


# CMP- matches those four characters literally.
# [0-9] matches one ASCII digit.
# {3} requires exactly three digits.
campaign_pattern = r"CMP-[0-9]{3}"

# | separates the three accepted alternatives.
# fullmatch() requires the whole input to match one alternative.
platform_pattern = r"Google|Meta|TikTok"

# [0-9] allows only ASCII digits.
# {1,5} requires between one and five digits.
# This accepts whole-euro amounts from 0 to 99999.
budget_pattern = r"[0-9]{1,5}"


# Nine checks: one accepted and two rejected values per field.
# Each tuple contains the pattern, input and expected result.
test_cases = [
    (campaign_pattern, "CMP-123", True),
    (campaign_pattern, "cmp-123", False),
    (campaign_pattern, "CMP-12", False),

    (platform_pattern, "Meta", True),
    (platform_pattern, "meta", False),
    (platform_pattern, "Facebook", False),

    (budget_pattern, "1500", True),
    (budget_pattern, "-50", False),
    (budget_pattern, "12.50", False)
]

print("Validation tests:")
passed = 0

for pattern, value, expected in test_cases:
    actual = re.fullmatch(pattern, value) is not None

    if actual == expected:
        status = "PASS"
        passed += 1
    else:
        status = "FAIL"

    print(
        f"{value!r}: expected={expected}, "
        f"actual={actual}, test={status}"
    )

print(f"Tests passed: {passed}/{len(test_cases)}")
print()

# All nine results match the expectations.
# A borderline case is "meta": it is rejected because
# my platform rule requires the exact spelling "Meta".


while True:
    campaign_id = input("Campaign ID (CMP-123): ").strip()
    platform = input("Platform (Google, Meta or TikTok): ").strip()
    budget = input("Budget in whole euros (0-99999): ").strip()

    valid_campaign = (
        re.fullmatch(campaign_pattern, campaign_id) is not None
    )

    valid_platform = (
        re.fullmatch(platform_pattern, platform) is not None
    )

    valid_budget = (
        re.fullmatch(budget_pattern, budget) is not None
    )

    if valid_campaign and valid_platform and valid_budget:
        break

    if not valid_campaign:
        print("Invalid ID. Use uppercase CMP- and three digits.")

    if not valid_platform:
        print("Invalid platform. Use Google, Meta or TikTok exactly.")

    if not valid_budget:
        print("Invalid budget. Enter one to five digits only.")

    print("Please enter the three fields again.\n")


# This section is reached only after all three fields pass.
file_path = Path("campaigns.csv")

needs_header = (
    not file_path.exists()
    or file_path.stat().st_size == 0
)

with open(file_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if needs_header:
        writer.writerow(["campaign_id", "platform", "budget_euros"])

    writer.writerow([campaign_id, platform, int(budget)])

print("All three fields are valid.")
print("Campaign saved to campaigns.csv.")