# Task - 3: Temperature Converter

print("Available Units: C - Celsius, F - Fahrenheit, K - Kelvin")
unit1 = input("Enter the current unit (C/F/K): ")
unit2 = input("Enter the unit to convert to (C/F/K): ")
temp = float(input("Enter the temperature value: "))

if unit1 == "C":
    if unit2 == "F":
        result = round((temp * 9/5) + 32, 2)
        print(f"\n{temp}°C = {result}°F")
    elif unit2 == "K":
        result = round(temp + 273.15, 2)
        print(f"\n{temp}°C = {result} K")
    elif unit2 == "C":
        print(f"\nNo conversion needed. Temperature = {temp}°C")
    else:
        print("\nInvalid Measurement unit.")

elif unit1 == "F":
    if unit2 == "C":
        result = round((temp - 32) * 5/9, 2)
        print(f"\n{temp}°F = {result}°C")
    elif unit2 == "K":
        result = round(((temp - 32) * 5/9) + 273.15, 2)
        print(f"\n{temp}°F = {result} K")
    elif unit2 == "F":
        print(f"\nNo conversion needed. Temperature = {temp}°F")
    else:
        print("\nInvalid Measurement unit.")

elif unit1 == "K":
    if unit2 == "C":
        result = round(temp - 273.15, 2)
        print(f"\n{temp} K = {result}°C")
    elif unit2 == "F":
        result = round(((temp - 273.15) * 9/5) + 32, 2)
        print(f"\n{temp} K = {result}°F")
    elif unit2 == "K":
        print(f"\nNo conversion needed. Temperature = {temp} K")
    else:
        print("\nInvalid Measurement unit.")

else:
    print("\nInvalid input unit.")
