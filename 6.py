# Tuple containing seasons in order: winter, spring, summer, autumn
seasons = ("Winter", "Spring", "Summer", "Autumn")


# Main program
def main():
    month = int(input("Enter the number of the month (1-12): "))

    if month < 1 or month > 12:
        print("Invalid month number. Must be between 1 and 12.")
        return

    # Map month to season
    if month in (12, 1, 2):
        season = seasons[0]  # Winter
    elif month in (3, 4, 5):
        season = seasons[1]  # Spring
    elif month in (6, 7, 8):
        season = seasons[2]  # Summer
    else:  # 9,10,11
        season = seasons[3]  # Autumn

    print(f"The season for month {month} is {season}.")


# Run the program
main()
