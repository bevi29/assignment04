def main():
    names = set()  # Store unique names
    while True:
        name = input("Enter a name (or press Enter to finish): ")
        if name == "":
            break
        if name in names:
            print("Existing name")
        else:
            print("New name")
            names.add(name)

    print("\nList of entered names:")
    for n in names:
        print(n)


# Run the program
main()
