# Define function
def mi_function(name, lastname):  # Function with parameter 'name'
    print(f'Hi your name is: {name} and your lastname is: {lastname}')


mi_function('Uriel', 'Castro')


# Use return
def sum(a, b):
    return a + b


result = sum(5, 3)
print(f'Summation result: {result}')
print(f'Summation result: {sum(5, 3)}')


# Use default parameters in function
# def sumar(a:int = 0, b:int = 0)  Define type of variables
def suma(a=0, b=0) -> int:  # Define type of return, but it is not obligatory return type int
    return a + b


print(f'Result: {suma(2, 8)}')


# X quantity Args in functions
def list_names(*names):  # Names are tuple
    for name in names:
        print(name)


list_names('Juan', 'Pedro', 'Uriel')


# Exercise args in function to sum
def summation(*numbers: int):
    resultado = 0
    for number in numbers:
        resultado += number
    return resultado


print(summation(2, 5, 7, 10))


def multiplication(*args: int):
    # Use pase to only define function and not generate error
    # pass
    resultado = 1
    for number in args:
        resultado *= number
    return resultado


print(multiplication(2, 5, 10))


# pass key, value to function or dictionaries
def list_terms(**kwargs):  # Kwargs don't necessary
    for key, value in kwargs.items():
        print(f'{key}: {value}')


list_terms(IDE='Integrated Development Environment', PK='Primary Key')


# pass list element to function
def display_names(names):
    for name in names:
        print(name)


names = ['Juan', 'Karla', 'Uriel']
display_names(names)
display_names('Carlos')  # Print ['C', 'a', 'r', 'l', 'o', 's']
display_names((10, 11))  # Sending (tuple) or [list] to function| display_names(10, 11) => error


# Recursive functions example with factorial | call the function to return 1 !!!Consult more information
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


print(factorial(5))
