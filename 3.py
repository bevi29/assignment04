# Function that converts gallons to liters
def gallons_to_liters(gallons):
    return gallons * 3.78541   # 1 US gallon ≈ 3.78541 liters

# Main program
def main():
    while True:
        gallons = float(input("Enter gasoline quantity in gallons (negative value to quit): "))
        if gallons < 0:
            print("Program ended.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons = {liters:.2f} liters")

# Run the program
main()
