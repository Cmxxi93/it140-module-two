"""Ask for a user's name and age and calculate their birth year.

Input:
    User's name as a string.
    User's age as an integer.

Process:
    Subtract the user's age from 2025.

Output:
    A greeting showing the user's name and approximate birth year.

Typical usage example:
    What is your name? Alex
    How old are you? 24
    Hello Alex! You were born in 2001.
"""

# === Constants ===
CURRENT_YEAR = 2025

# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input
    name = input("What is your name? ")
    age = int(input("How old are you? "))

    # Calculate approximate birth year
    birth_year = CURRENT_YEAR - age

    # Display personalized message
    print(f"Hello {name}! You were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()

