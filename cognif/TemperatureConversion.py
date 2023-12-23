def convert_temperature():
    temp = float(input("Enter temperature value: "))
    unit = input("Enter unit of measurement (C/F): ")
    if unit == "C":
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {fahrenheit:.2f}°F")
    elif unit == "F":
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid unit of measurement. Please enter either 'C' or 'F'.")

convert_temperature()