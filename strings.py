# Strings

# SINGLE_QUOTES = 'Look Single quotes '
# Double_qoutes = "look double quotes"
#
# print(SINGLE_QUOTES)
# print(Double_qoutes)
#
# # string_failure = 'i said 'wow!'
#
# escape_example = 'i said \'wow\''\
# print(escape_example)
# quote_in_quote = 'I said "wow!"'
# print(quote_in_quote)
# reverse_quote = "i said 'wow!"
# print(reverse_quote)


# String slicing


#Everything in code starts with 0 not 1
# H E L L O W O R L D !
# 0 1 2 3 4 5 6 7 8 9 10

Hw = "hello world!"
print (Hw[7:]) #orld!
print(Hw[-5:])# orld!
print(Hw[:5]) # Hello
print(Hw[0:5]) # slice strings how you would slice a cake

# String methods


# strip()

white_space = "lots of space at the end                       "
print (len(white_space)) #47

print(len(white_space.strip())) #24

# A Few more

example_text =" Here's some text with lots of text"
# count a substring within a stiring
print(example_text.count("'"))

# Make everything lower case
print(example_text.lower())

# Make everything upper case
print(example_text.upper())


# Capitslidr thinhs
print(example_text.capitalize())

# Replace text
print(example_text.replace("with" ,"," ))
# Concatention

a = "here "
b = "more "
c = "much more "
print(a + b +c)

# casting

# x = 2
# y = 5.4
# z = " there a number 25.4 unless we put a space!"
# # print(x + y + z)
# print(str(x) + str(y) + z)
#
# #String to numberic
# int_string = "6"
# print(int)(int_string))
# print(type)(int)(int_string)))

# F-strings (formated strings)

# name = "lassie"
# years = 7
# height_cm = 60.2
# print(f"{name} is {years} years old and {height_cm}cm tall")
#
# # F- strings allow us to use methods/ evaulations too

name = "Snoopy"
years = 52

print(f"{name.upper()} is {years * 7} years old in dog years")

#F strind yo specify precision in rounding and decimals

pi = 3.14159265359
print(f"pi to 3 decimal placed: {pi:.3f}") # pi to 3 decimal places
print(f"pi to 3 decimal placed: {pi:.5f}") # pi to 5 decimal places

score = 16
max_score = 26
print(f"you scored {score/max_score}")
print(f"you scored {score/max_score:%}") #61.53
print(f"you scored {score/max_score:.2%}")

