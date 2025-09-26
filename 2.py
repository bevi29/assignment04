import random

# Function that returns a random dice roll between 1 and "sides"
def roll_dice(sides):
    return random.randint(1, sides)

# Main program
def main():
    sides = int(input("Enter the number of sides on the dice: "))
    result = 0
    while result != sides:   # Keep rolling until we hit the maximum
        result = roll_dice(sides)
        print(f"Rolled: {result}")

# Run the program
main()
