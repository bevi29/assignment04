import math


# Function to calculate pizza unit price per square meter
def pizza_unit_price(diameter_cm, price_eur):
    radius_m = (diameter_cm / 2) / 100  # Convert radius to meters
    area_m2 = math.pi * radius_m ** 2  # Area in square meters
    unit_price = price_eur / area_m2
    return unit_price


# Main program
def main():
    # Get data for first pizza
    diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
    price1 = float(input("Enter the price of the first pizza (€): "))

    # Get data for second pizza
    diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
    price2 = float(input("Enter the price of the second pizza (€): "))

    # Calculate unit prices
    unit1 = pizza_unit_price(diameter1, price1)
    unit2 = pizza_unit_price(diam
