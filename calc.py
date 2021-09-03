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
            n = int(input("First Number: "))
            time.sleep(0.5)
            n1 = int(input("Second Number: "))
            sum = int(n + n1)
            print(f'{n} + {n1} = {sum}')
            break
        if args == '3':
            n = int(input("First Number: "))
            time.sleep(0.5)
            n1 = int(input("Second Number: "))
            time.sleep(0.5)
            n2 = int(input("Third Number: "))
            sum = int(n + n1 + n2)
            print(f'{n} + {n1} + {n2} = {sum}')
            break
        if args == '4':
            n = int(input("First Number: "))
            time.sleep(0.5)
            n1 = int(input("Second Number: "))
            time.sleep(0.5)
            n2 = int(input("Third Number: "))
            time.sleep(0.5)
            n3 = int(input("Fourth Number: "))
            sum = int(n + n1 + n2 + n3)
            print(f'{n} + {n1} + {n2} + {n3} = {sum}')
            break