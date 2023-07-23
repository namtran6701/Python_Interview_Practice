# check how self work 
class my_dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print('Gau gau')

    def get_name(self):
        print(f'My name is {self.name}')

    def get_age(self):
        print(f'I am {self.age} years old')


good_dog = my_dog('boyu', 22)
good_dog.bark()

# check if the class would reuire users to provide inputs in the __init__ method
class my_bank:
    def __init__(self, initial_amount):
        self.initial_amount = initial_amount
    def deposit(self, amount_deposit):
        initial_amount += amount_deposit
        
# check inheritance

class bank_rp(my_bank):
    def get_report(self):
        print(f'The current amount is {self.initial_amount}')

nam_bank = bank_rp(500)

nam_bank.get_report()