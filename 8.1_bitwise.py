"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,
       such as who may view, edit and publish a campaign.

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In:
# Three permissions for a sales management system:
# VIEW_SALES = 001: view sales figures.
# EDIT_SALES = 010: edit sales figures.
# EXPORT_REPORT = 100: export a sales report.

# 2. Process:
# Combine VIEW_SALES and EDIT_SALES using bitwise OR.
# Test whether EXPORT_REPORT is present using bitwise AND.
# Add EXPORT_REPORT using bitwise OR.
# Remove EDIT_SALES using bitwise AND with its inverted mask.

# 3. Out:
# The permissions are displayed in binary at each step.
# The program also displays whether export permission is present.

# 4. What my permissions are about:
# These permissions control access to a sales dashboard.
# An employee may view sales, correct figures or export reports.
# Separate bits allow these permissions to be managed independently.


VIEW_SALES = 0b001
EDIT_SALES = 0b010
EXPORT_REPORT = 0b100

# Bit order from left to right: Export, Edit, View.
print("Bit order: Export | Edit | View")
print()

print(f"VIEW_SALES:    {VIEW_SALES:03b}")
print(f"EDIT_SALES:    {EDIT_SALES:03b}")
print(f"EXPORT_REPORT: {EXPORT_REPORT:03b}")
print()

# Step 1: Combine two permissions.
permissions = VIEW_SALES | EDIT_SALES

print(f"Step 1 - Combine view and edit: {permissions:03b}")

# Step 2: Check whether the third permission is present.
export_mask = permissions & EXPORT_REPORT
has_export = bool(export_mask)

print(f"Step 2 - Export check mask:     {export_mask:03b}")
print("Has export permission:", has_export)

# Step 3: Add the third permission.
permissions |= EXPORT_REPORT

print(f"Step 3 - Add export:            {permissions:03b}")
print("Has export permission:", bool(permissions & EXPORT_REPORT))

# Step 4: Remove edit permission.
permissions &= ~EDIT_SALES

print(f"Step 4 - Remove edit:           {permissions:03b}")

print()
print("Final permissions:")
print("Can view sales:", bool(permissions & VIEW_SALES))
print("Can edit sales:", bool(permissions & EDIT_SALES))
print("Can export reports:", bool(permissions & EXPORT_REPORT))

# Manual checks:
# 001 | 010 = 011: view and edit are enabled.
# 011 & 100 = 000: export is absent.
# 011 | 100 = 111: all three permissions are enabled.
# 111 & ~010 = 101: export and view remain enabled.
