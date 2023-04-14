def Calcule(num1, operator, num2):
    if operator == '+' :
        return num1 + num2
    elif operator == "-" :
        return num1 - num2
    elif operator == '*' :
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else :
        return("Impossible")

print(Calcule(10, '+', 14))
print(Calcule(10, '-', 14))
print(Calcule(10, '*', 14))
print(Calcule(10, '/', 14))
print(Calcule(10, '%', 14))
print(Calcule(10, 'ok', 14))