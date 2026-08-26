from pyscript import display, document
# Drill 2


# Adds the two values
def addition(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    sum = num_1 + num_2

    display(f'The sum of {num_1} and {num_2} is {sum}.', target='result')

# Subtracts the two values
def subtraction(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    diff = num_1 - num_2

    display(f'The difference of {num_1} and {num_2} is {diff}.', target='result')

# Multiplies the two values
def multiply(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    prod = num_1 * num_2

    display(f'The product of {num_1} and {num_2} is {prod}.', target='result')

# Divides the two values
def divide(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    quot = num_1 / num_2

    display(f'The quotient of {num_1} and {num_2} is {quot}.', target='result')

# Finds the remainder between the two values when divided
def modulate(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    rem = num_1 % num_2

    display(f'The remainder of {num_1} and {num_2} is {rem}.', target='result')

# Raises the first value to the power of the second
def exponent(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    pow = num_1 ** num_2

    display(f'{num_1} to the power of {num_2} is {pow}.', target='result')

# Rounds off the result of the two values when divided
def floor(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    floor = num_1 // num_2

    display(f'The quotient of {num_1} and {num_2} rounded off is {floor}.', target='result')
