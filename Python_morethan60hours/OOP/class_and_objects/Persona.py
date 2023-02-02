# Init = initializer to add attributes

class Person:
    # Note method is equal to func but in class
    def __init__(self, name, lastname, age):  # this is method | Constructor | self is a variable can use this
        self.name = name  # are attributes
        self.lastname = lastname
        self.age = age

    def show_details(self):
        print(f'Person: {self.name}, {self.lastname}, {self.age}')


Person1 = Person('Juan', 'Perez', 28)  # this is an object
print(f'Person 1: {Person1.name}, {Person1.lastname}, {Person1.age}')
# Change attributes
Person1.name = 'Juan Carlos'
Person1.lastname = 'Reinaldo'
Person1.age = 20
print(f'Person 1: {Person1.name}, {Person1.lastname}, {Person1.age}')

# Call methods
Person1.show_details()
Person.show_details(Person1)  # Reference passed but not recommended

Person2 = Person('Julia', 'Martinez', 30)
print(f'Person 2: {Person2.name}, {Person2.lastname}, {Person2.age}')

# Add attributes to object
Person1.tel = '3006450160'
print(Person1.tel)
