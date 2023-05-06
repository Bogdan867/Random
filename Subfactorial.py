import sys
import math
import decimal

def subfactorial_helper(helper_num, memo):
    if helper_num in memo:
        return memo[helper_num]
    if helper_num == 0:
        return 1
    if helper_num == 1:
        return 0
    try:
        result = (helper_num - 1) * (subfactorial_helper(helper_num - 1, memo) + subfactorial_helper(helper_num - 2, memo))
        memo[helper_num] = result
        return result
    except RecursionError:
        raise ValueError('This number is too big to calculate using recursion')

def stirling_approximation(approximation_num):
    decimal.getcontext().prec = approximation_num + 1
    e = decimal.Decimal(math.e)
    factor = decimal.Decimal(math.factorial(approximation_num))
    series = sum([((-1)**k) / decimal.Decimal(math.factorial(k)) for k in range(approximation_num)])
    return (factor / e) * series

def subfactorial():
    subfactorial_loop = True
    while subfactorial_loop is True:
        subfactorial_num = input('Enter a non-negative integer (or "exit" to quit): ')
        if subfactorial_num == 'exit':
            subfactorial_loop = False
        try:
            subfactorial_num = int(subfactorial_num)
            if subfactorial_num < 0:
                raise ValueError('Input must be a non-negative integer')
            if subfactorial_num > 100020:
                result = stirling_approximation(subfactorial_num)
            else:
                result = subfactorial_helper(subfactorial_num, {})
            print(f'!{subfactorial_num} = {result}')
        except ValueError as e:
            print(f'Error: {e}')


def factorial():
    factorial_loop = True
    print('Welcome to the factorial calculator')
    while factorial_loop is True:
        factorial_num = input('Enter a non-negative integer (or "exit" to quit): ')
        if factorial_num == 'exit':
            print('Exiting program, goodbye!')
            factorial_loop = False
        try:
            factorial_num = int(factorial_num)
            if factorial_num < 0:
                raise ValueError('Input must be a non-negative integer')
            if factorial_num > 100000001:
                raise ValueError('Input number is too big to calculate using math.factorial')
            result = math.factorial(factorial_num)
            print(f'{factorial_num}! = {result}')
        except ValueError as e:
            print(f'Error: {e}')

def menu():
    menu_loop = True
    while menu_loop is True:
        print('''
<---------------MENU--------------->
Hello and welcome. Choose function:

1) Factorial
2) Subfactorial
3) Exit
<---------------MENU--------------->
''')
        choice = input('Enter your choice: ').lower()
        if choice == '1':
            factorial()
        elif choice == '2':
            subfactorial()
        elif choice == '3' or choice == 'exit':
            print('OK, see you soon. Goodbye!')
            menu_loop = False
        else:
            print(f'There is no {choice} punct, try again')

menu()





