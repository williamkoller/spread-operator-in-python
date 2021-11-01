"""
    * Function Arguments
"""


def multiply(a: float, b: float) -> float:
    return a * b


numbers = [3, 5]

print(multiply(*numbers))

"""
    * Array Literals
"""
number_s = [1, 2, 3, 4]

new_numbers = [0, *number_s, 5]

print(new_numbers)


""" 
    * Object Literals
"""
person = {
    'name': 'William',
    'surname': 'Koller'
}

print({**person, 'age': 32})
