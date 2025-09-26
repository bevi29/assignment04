# Function that removes odd numbers from a list
def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]


# Main program
def main():
    # Example list
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Get list without odd numbers
    even_list = remove_odds(original_list)

    # Print results
    print("Original list:", original_list)
    print("Even-only list:", even_list)


# Run the program
main()
