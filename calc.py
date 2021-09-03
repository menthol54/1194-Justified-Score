import math
import time

def add():
    print("How many numbers?")
    args = input('')
    while True:
        if args == '1':
            print("Are you serious?")
            return
        if args == '2':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            sum = float(n + n1)
            print(f'{n} + {n1} = {sum}')
            break
        if args == '3':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            time.sleep(0.5)
            n2 = float(input("Third Number: "))
            sum = float(n + n1 + n2)
            print(f'{n} + {n1} + {n2} = {sum}')
            break
        if args == '4':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            time.sleep(0.5)
            n2 = float(input("Third Number: "))
            time.sleep(0.5)
            n3 = float(input("Fourth Number: "))
            sum = float(n + n1 + n2 + n3)
            print(f'{n} + {n1} + {n2} + {n3} = {sum}')
            break
def sub():
    print("How many numbers?")
    args = input('')
    while True:
        if args == '1':
            print("Are you serious?")
            return
        if args == '2':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            sum = float(n - n1)
            print(f'{n} - {n1} = {sum}')
            break
        if args == '3':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            time.sleep(0.5)
            n2 = float(input("Third Number: "))
            sum = float(n - n1 - n2)
            print(f'{n} - {n1} - {n2} = {sum}')
            break
        if args == '4':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            time.sleep(0.5)
            n2 = float(input("Third Number: "))
            time.sleep(0.5)
            n3 = float(input("Fourth Number: "))
            sum = float(n - n1 - n2 - n3)
            print(f'{n} - {n1} - {n2} - {n3} = {sum}')
            break
