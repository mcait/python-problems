def print_multiplication_table(n):
    number1 = 1 
    while number1 <= n:
        number2 = 1
        while number2 <= n:
            print number1, "*", number2, "=", (number1 * number2)
            number2 = number2 + 1
        number1 = number1 + 1