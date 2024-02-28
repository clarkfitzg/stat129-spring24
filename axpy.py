
def add1(x):
    return x + 1

a = 10
b = add1(a)

# What's the value of b?


def add1(x):
    """
    Add 1 to x

    It's so easy to document Python code!
    """
    # Notes for someone reading the code  (comment)
    return x + 1


def foo(a, x, y):
    ax = a*x
    return ax + y

foo(2, 3, -1)


def axpy(a, x, y):
    ax = a*x
    return ax + y


axpy(a=2, x=5, y=10)  # Want: 2*5 + 10

axpy(a=2, x=5)  # Want: 2*5

axpy(x=5, y=10) # Want: 5+10

axpy(5)


def axpy2(a=1, x, y=0):
    ax = a*x
    return ax + y




def add(x, y=1):
    return x + y




def foo(a, x, y):
    ax = a*x
    return ax + y


def celsius_to_fahrenheit(degC=0):
    """
    Convert temperature from degrees
    Celsius into Fahrenheit
    """
    return degC * (9/5) + 32

celsius_to_fahrenheit(0)  # 32, freezing

celsius_to_fahrenheit(40) # 104, HOT

import random

def bar(stream, prob=0.5):
    """
    Return each element from stream with some probability
    """
    result = []
    for x in stream:
        # Randomly True or False
        include = random.choice([True, False], weights=[prob, 1-prob])
        if include:
            result.append(x)
    # Loop is over
    return result


import random

def bar(stream, prob=0.5):
    """
    Return each element from stream with some probability
    """
    result = []
    for x in stream:
        # Randomly True or False
        include = random.choices([True, False], weights=[prob, 1-prob])
        # Got a random True
        if include[0]:
            # Store it in the result
            result.append(x)
    # All done!        
    return result

bar("abcdefghijklm")

bar(range(10))
