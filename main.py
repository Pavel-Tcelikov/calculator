from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.BLACK)
print(Back.GREEN)

What = input("Что делаем? (+, -, *, /, //, %): ")

print(Back.CYAN)

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print(Back.YELLOW)

if What == "+":
    с = a + b
    print(с)
elif What == "%":
    c = a % b
    print(c)
elif What == "//":
    c = a // b
    print(c)
elif What == "-":
    c = a - b
    print(c)
elif What == "*":
    c = a * b
    print(c)
elif What == "/":
    c = a / b
    print(c)
else:
    print("Выбрана не верная операция!")

input()
