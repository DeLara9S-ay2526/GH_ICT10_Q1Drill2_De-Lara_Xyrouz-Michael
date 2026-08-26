from pyscript import display, document
# Drill 2


def addition(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    sum = num_1 + num_2

    display(f'The sum of {num_1} and {num_2} is {sum}.', target='result')

def subtraction(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    diff = num_1 - num_2

    display(f'The difference of {num_1} and {num_2} is {diff}.', target='result')

def multiply(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    prod = num_1 * num_2

    display(f'The product of {num_1} and {num_2} is {prod}.', target='result')

def divide(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    quot = num_1 / num_2

    display(f'The quotient of {num_1} and {num_2} is {quot}.', target='result')

def modulate(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    rem = num_1 % num_2

    display(f'The remainder of {num_1} and {num_2} is {rem}.', target='result')

def exponent(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    pow = num_1 ** num_2

    display(f'{num_1} to the power of {num_2} is {pow}.', target='result')

def floor(e):
    document.getElementById('result').innerHTML = " "
    num_1 = float(document.getElementById('num1').value)
    num_2 = float(document.getElementById('num2').value)
    floor = num_1 // num_2

    display(f'The quotient of {num_1} and {num_2} rounded off is {floor}.', target='result')