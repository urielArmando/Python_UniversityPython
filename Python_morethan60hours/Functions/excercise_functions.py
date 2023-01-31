# Print numbers sort descending
def sort_numbers(number):
    if number >= 1:
        print(number)
        sort_numbers(number-1)
    elif number < 1:
        return 'Value incorrect...'


print(sort_numbers(3))


# Exercise calculator of taxes
def calculator_taxes(taxes_applied, amount_taxes):
    total = taxes_applied + taxes_applied * (amount_taxes/100)
    print(f'Pago con impuestos: {total}')


taxes_applied = int(input('Proporcione el pago sin impuesto: \n>>'))
amount_applied = int(input('Proporcione el monto del impuesto: \n>>'))
calculator_taxes(taxes_applied, amount_applied)


# Converse temperature to Fahrenheit
def fahrenheit_to_celsius(degrees: float):
    return (degrees - 32) * 5/9


# Converse temperature to Celsius
def celsius_to_fahrenheit(degrees: float):
    return degrees * 9/5 + 32


celsius = float(input('Give degrees in celsius: '))
result_celsius = celsius_to_fahrenheit(celsius)
print(f'{celsius}°C to F: {result_celsius:.2f}°F')

fahrenheit = float(input('Give degrees in fahrenheits: '))
result_fahrenheit = fahrenheit_to_celsius(fahrenheit)
print(f'{fahrenheit}°F to C: {result_fahrenheit:.2}°C')

