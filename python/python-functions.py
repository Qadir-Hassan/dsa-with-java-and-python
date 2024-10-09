"""
Q1. Basic Function: Write a function multiply that takes two arguments and returns their product.
"""

def multiply(num1, num2):
    return(num1 * num2)
# Call the Multiply Function
print(multiply(3,5))

"""
Q2. Using *args: Write a function sum_all that accepts any number of arguments 
    using *args and returns the 
    sum of all the numbers.
"""

def sum_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
# Call the sum_all Function
print(sum_all(4,6,8,9,))

"""
Q3. Using **kwargs: Write a function greet that accepts any number of keyword arguments 
    and returns a greeting message in the format: '"Hello Qadir Hassan, you are 25 years old."'
"""

def greet(**kwargs):
    
    for key,value in kwargs.items():
       
     
       fname = kwargs.get('fname', 'Unknown')
       lname = kwargs.get('lname', 'Unknown')
       age = kwargs.get('age', 'Unknown')

    return f"Hello,{fname +" "+ lname} you are {age} old"
    
print(greet(fname ="qadir", lname="Hassan", age = 25))

"""
Combining *args and **kwargs: Write a function print_info that accepts any number 
of positional arguments and keyword arguments. Print the positional arguments as a list and 
the keyword arguments as a dictionary.
"""

def print_info(*args, **kwargs):
    print(args)
    for i in args:
        print(i)
    for key , value in kwargs.items():
        print(key,value)

   

print_info(2, "qadir", name="Hassan",age="20")