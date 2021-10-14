import time


def add():
    args = input("Enter all the numbers to be added, separated by a space:\n")
    end_value = 0

    args = args.split()

    try:
        for x in args:
            end_value += int(x)
    except ValueError:
        print("Improper value, only use numbers...")
        return add()

    print(end_value)


def sub():
    args = input("Enter all the numbers to be subtracted, separated by a space:\n")

    args = args.split()

    try:
        end_value = int(args[0])
        for x in args[1:]:
            end_value -= int(x)
    except ValueError:
        print("Improper value, only use numbers...")
        return sub()

    print(end_value)


def times():
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
            sum_num = float(n + n1)
            print(f'{n} + {n1} = {sum_num}')
            break
        if args == '3':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            time.sleep(0.5)
            n2 = float(input("Third Number: "))
            sum_num = float(n + n1 + n2)
            print(f'{n} + {n1} + {n2} = {sum_num}')
            break
        if args == '4':
            n = float(input("First Number: "))
            time.sleep(0.5)
            n1 = float(input("Second Number: "))
            time.sleep(0.5)
            n2 = float(input("Third Number: "))
            time.sleep(0.5)
            n3 = float(input("Fourth Number: "))
            sum_num = float(n + n1 + n2 + n3)
            print(f'{n} + {n1} + {n2} + {n3} = {sum_num}')
            break
        return times()


def div():
    print("How many numbers?")
    args = input('')
    while True:
        if type(args) != int:
            return args
        if type(args) == int:
            n = float(input("First Number:"))
            n1 = float(input("Second Number: "))
            sum_num = float(n / n1)
            print(f'{n} divided by {n1} = {sum_num}')
            break
        return div()
