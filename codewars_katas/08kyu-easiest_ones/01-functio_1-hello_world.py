# Make a simple function called greet that returns the most-famous "hello world!".
# https://www.codewars.com/kata/523b4ff7adca849afe000035

# Write a function `greet` that returns "hello world!"

# My solution


def greet():
    return u'hello world!'

pGreet = lambda : print(greet())

pGreet()

# Other people's solution I found interesting

# Other solution 1 - the " madman "

from subprocess import check_output
greet = lambda: check_output(["python3", "-c", "import __hello__"]).decode('ascii').lower()[:-1]

pGreet()

# https://www.codewars.com/kata/reviews/5485e5af4a0944ae2200016b/groups/5c55929f052d1c0001061eb0

# Other solution 2 - lambda

greet = lambda: "hello world!" 

pGreet()


# https://www.codewars.com/kata/reviews/5485e5af4a0944ae2200016b/groups/5c37ab89bad70c000164b32a

# Other solution 3 - %s

def greet():
    return "he%sworld!" %("llo ")

pGreet()

# https://www.codewars.com/kata/reviews/5485e5af4a0944ae2200016b/groups/5c4324a65c79950001515029

"""

➜ python3 01-functio_1-hello_world.py
hello world!
hello world!
hello world!
hello world!

"""
