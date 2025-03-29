FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
 
def convert_to_celsius(fahrenheit):
    
    celcius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    return round(celcius, 2)

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return round(fahrenheit, 2)

input_temp = float(input("Enter the temperature to convert: ").strip())
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if temp_unit == "C":
    converted_temp = convert_to_fahrenheit(input_temp)
    print(f"{input_temp}°C  is {converted_temp} °F.")
elif temp_unit == "F":
    converted_temp = convert_to_celsius(input_temp)
    print(f"{input_temp}°F is {converted_temp} °C.")
else:
    print("Invalid temperature unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    