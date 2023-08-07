import pylint
from statistics import mean, stdev
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


# Practice with class 

'''
Problem 1: 

Create a class named BankAccount with attributes account_holder_name, balance, and account_number.
Include methods to deposit, withdraw, and display_balance.
Ensure that the balance can't go negative.

'''
class BankAccount:
    def __init__(self, account_holder_name, balance, account_number):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_number = account_number
    def deposit(self, amount):
        if amount <0:
            print('Deposit invalid')
        else:
            self.balance += amount 
            print(f'Deposit {amount} successfully, the new balance is {self.balance}')
    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print('Fund is insufficient')
        elif withdraw_amount <0:
            print('Cannot withdraw a negative amount')
        else:
            self.balance -= withdraw_amount
            print(f'Withdraw {withdraw_amount} successfully, the new balance is {self.balance}')
    def display_balance(self):
        print(f'The current account balance is {self.balance}')


Nam_bank = BankAccount('Nam Tran', 1000, 6702001)
Nam_bank.display_balance()
Nam_bank.withdraw(500)
Nam_bank.deposit(100)


'''
Problem 2: 
Student Management System:

Create a class Student with attributes name, student_id, and grades (a list).
Implement methods to calculate the student's average grade and a method to display their information.

Create a class Course with attributes like course_name and students (a list of Student objects).
Implement methods to add_student, remove_student, and average_course_grade.

'''

class Student:
    def __init__(self, name, student_id):
         self.student_id = student_id
         self.name = name
         self.grades = []
    def mean_grade(self):
        if self.grades:
            ave_grade = mean(self.grades)
            return ave_grade
        else:
           return 'Student has no grade'

    def import_grade(self, grade):
        if type(grade) == int:
            self.grades.append(grade)
        else:
            print('Please import valid grade')
    def student_info(self):
        print(f'Student Nam: {self.name}')
        print(f'Student ID {self.student_id}')
        print(f'Average grade is {self.mean_grade()}')
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = [] 
    def enroll_student(self, new_student_id):
        if new_student_id not in self.students:
            self.students.append(new_student_id)
    def remove_student(self, student_id):
        if student_id in self.students:
            self.students.remove(student_id)
    def course_info(self):
        print(f'The course name is {self.course_name}')
        print(f'Total number of students in the class is {len(self.students)}')

student_1 = Student('Nam', 'N04058239')
student_1.import_grade(100)
student_1.import_grade(90)
student_1.student_info()

math = Course('Math')

math.enroll_student('Nam')
math.enroll_student('Lee')
math.enroll_student('Boyu')

math.course_info()