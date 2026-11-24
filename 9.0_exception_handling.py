"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The user enters the number of conversions for a campaign.
# The campaign cost is fixed at 1000 euros.

# 2. Process:
# Convert the input to a number.
# Divide the campaign cost by the number of conversions.
# Handle invalid text and division by zero separately.
# Allow unlimited attempts until a valid calculation succeeds.

# 3. Out:
# The cost per conversion in euros.
# If the input is invalid, display a helpful message and ask again.

# 4. The two failures, and whether they deserve the same message:
# ValueError: text or an empty input cannot be converted to a number.
# ZeroDivisionError: the number is zero, so division is impossible.
# They need different messages because the user must fix different problems.
# Separate exception handlers explain the exact problem.
# Catching every error together could hide unrelated programming mistakes.

# Four checks and their expected behaviours:
# 1. Input "20": display 50.00 euros and finish successfully.
# 2. Input "0": explain that zero conversions cannot be a divisor; ask again.
# 3. Input "abc": explain that a number is required; ask again.
# 4. Empty input: explain that nothing was entered; ask again.
# For checks 2, 3 and 4, entering "20" afterwards completes the calculation.


import math


campaign_cost = 1000

while True:
    try:
        user_input = input("Enter the number of conversions: ").strip()
    except EOFError:
        print("\nInput closed. Program ended safely.")
        break
    except KeyboardInterrupt:
        print("\nProgram stopped by the user.")
        break

    try:
        conversions = float(user_input)

        if not math.isfinite(conversions):
            print("Please enter a finite number.")
            continue

        if conversions < 0:
            print("Conversions cannot be negative. Please try again.")
            continue

        cost_per_conversion = campaign_cost / conversions

        if not math.isfinite(cost_per_conversion):
            print("The number is too small. Please enter a larger number.")
            continue

    except ValueError:
        if user_input == "":
            print("You entered nothing. Please type a number.")
        else:
            print("Invalid input. Please enter a number, for example 20.")

    except ZeroDivisionError:
        print("Cannot calculate cost per conversion with zero conversions.")
        print("Please enter a number greater than zero.")

    else:
        print(f"Cost per conversion: {cost_per_conversion:.2f} euros")
        break
    
