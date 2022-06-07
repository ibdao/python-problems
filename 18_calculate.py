def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, raise error:

        >>> calculate('foo', 2, 3)
        Traceback (most recent call last):
          ...
        ValueError: Invalid Operation
    """
    if operation == 'add':
        if make_int == True:
            return f"{message} {int(add(a,b))}"
        else:
            return f"{message} {add(a,b)}"
    elif operation == 'subtract':
        if make_int == True:
            return f"{message} {int(subtract(a,b))}"
        else:
            return f"{message} {subtract(a,b)}"
    elif operation == 'multiply':
        if make_int == True:
            return f"{message} {int(multiply(a,b))}"
        else:
            return f"{message} {multiply(a,b)}"
    elif operation == 'divide':
        if make_int == True:
            return f"{message} {int(divide(a,b))}"
        else:
            return f"{message} {divide(a,b)}"
    else:
        raise ValueError("Invalid Operation")



def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def subtract(a, b):
    return a - b
def divide(a, b):
    return a/b




