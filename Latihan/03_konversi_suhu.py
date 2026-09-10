KELVIN_OFFSET = 273.15

celcius = float(input("Masukan suhu dalam Celcius:"))

fahrenheit = ( 9 / 5 * celcius) + 32
kelvin = celcius + KELVIN_OFFSET

print(f"Fahrenheit = {fahrenheit: .2f}")
print(f"Kelvin: {kelvin: .2f}")