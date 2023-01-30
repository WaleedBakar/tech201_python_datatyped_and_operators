# tech201_python_datatyped_and_operators
_python_datatyped_and_operators
# Strings
Strings are sequences of characters that are used to store and represent text-based information. In Python, strings are created by enclosing characters in single or double quotes. For example, the following code creates two strings: 
````
x = '2' 
y = "5.4"
````
We can use the + operator to concatenate (or join) strings together. For example, the following code prints the concatenated string of x, y, and z: 
````
z = "there a number 25.4 unless we put a space!"
print(x + y + z)
````
However, if we try to add a number and a string together, we will get an error. This is because Python interprets the number as an integer, and it cannot add an integer to a string. To fix this, we can use the str() function to convert the number to a string. For example: 
````
print(str(x) + str(y) + z)
````
We can also use the int() function to convert strings to numbers. For example: 
````
int_string = '6'
print(int(int_string))
print(type(int(int_string)))
````
F-strings (formatted strings) are a way to format strings in Python. They allow us to insert variables and expressions directly into a string. For example: 
``````
name = 'Lassie'
years = 7
height_cm = 60.2
print(f'{name} is {years} years old and {height_cm}cm tall')
``````
F-strings also allow us to use methods and evaluations. For example: 
````
name = 'Snoopy'
years = 52
print(f'{name.upper()} is {years * 7} years old in dog years')
````
F-strings can also be used to specify precision in rounding and decimals. For example: 
``````
pi = 3.14159265359
print(f'pi to 3 decimal places: {pi:.3f}')
print(f'pi to 5 decimal places: {pi:.5f}')
``````
Finally, F-strings can be used to format percentages. For example: 
````
score = 16
max_score = 26
print(f'you scored {score/max_score}')
print(f'you scored {score/max_score:%}') #61.53
print(f'you scored {score/max_score:.2%}') #61.53%.
````

# Booleans
Booleans are a data type in Python that can have one of two values: True or False. They are useful for quickly checking the state of something, such as whether a number is greater than or equal to another number, or whether a string is empty or not. They can also be used to validate data types, such as whether a string is composed of only letters or not.

In Python, we can use the == operator to compare two values and return a boolean. For example, if we have two variables, a and b, and set them to True and False respectively, we can use the == operator to check if they are equal:
````
a = True
b = False

print(a == b) # False
````
We can also use the != operator to check if two values are not equal:
````
print(a != b) # True
````
We can also use the &gt;= and &lt;= operators to check if one value is greater than or equal to, or less than or equal to another value:
``````
print(a &gt;= b) # True
print(a &gt;= True) # True
print(b &lt;= False) # True
```````
We can also combine two booleans using the and and or operators. The and operator will return True only if both values are True, while the or operator will return True if either value is True:
````
print(True and False) # False
print(False and True) # False
print((False or True) # True
````
We can also check if a variable is None by using the == operator or the is operator. The == operator will check if the variable is equal to None, while the is operator will check if the variable is the same object as None:
````
x = None

print(x == False) # False
print(x == None) # True
print(x is None) # True
````
We can also use the type() function to check the type of a variable. If the variable is None, the type() function will return NoneType:
````
print(type(x)) # <class 'nonetype'="">
````
Booleans are a powerful tool in Python that can be used to quickly check the state of something or validate data types.</class>

