"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""

# Your code below
# 1. In:
# Two strings: "Sales" and "sales".

# 2. Process:
# Compare the strings using ==, !=, <, <=, > and >=.
# Combine comparison results using and, or and not.
# Compare the actual results with my predictions.

# 3. Out:
# A readable table showing each expression,
# its predicted result and its actual result.
# The number of correct predictions is displayed at the end.

# 4. My chosen values and a surprising comparison:
# I chose "Sales" and "sales".
# The interesting result is that "Sales" < "sales" is True.
# Python compares strings lexicographically by Unicode code point.
# Uppercase "S" has a smaller code point than lowercase "s".


a = "Sales"
b = "sales"

# Predictions are written before running the comparisons.
predictions = [
    False,  # a == b
    True,   # a != b
    True,   # a < b
    True,   # a <= b
    False,  # a > b
    False,  # a >= b
    True,   # (a < b) and (a != b)
    False,  # (a == b) or (a > b)
    True    # not (a == b)
]

results = [
    ("a == b", a == b),
    ("a != b", a != b),
    ("a < b", a < b),
    ("a <= b", a <= b),
    ("a > b", a > b),
    ("a >= b", a >= b),
    ("(a < b) and (a != b)", (a < b) and (a != b)),
    ("(a == b) or (a > b)", (a == b) or (a > b)),
    ("not (a == b)", not (a == b))
]

print("a =", repr(a))
print("b =", repr(b))
print()

print(f"{'Expression':<28} {'Prediction':<12} {'Actual':<12}")
print("-" * 54)

correct = 0

for index, (expression, actual) in enumerate(results):
    predicted = predictions[index]

    print(f"{expression:<28} {str(predicted):<12} {str(actual):<12}")

    if predicted == actual:
        correct += 1

print()
print(f"Correct predictions: {correct}/{len(results)}")