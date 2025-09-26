import random

# Function that returns a random dice roll between 1 and 6
def roll_dice():
    return random.randint(1, 6)

# Main program
def main():
    result = 0
    while result != 6:
        result = roll_dice()
        print(f"Rolled: {result}")

# Run the program
main()


