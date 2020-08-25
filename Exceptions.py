# how to handle errors in your program 

try:
    age = int(input('age: '))
    print(age)
except ValueError:
    print('invalid value')    




try:
    age = int(input('age: '))
    income = 2000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age cannot be 0.')    