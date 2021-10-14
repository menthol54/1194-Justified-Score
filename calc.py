

def add():
    args = input("Enter all the numbers to be added, separated by a space:\n")

    args = args.split()

    try:
        end_value = int(args[0])
        for x in args[1:]:
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
    args = input("Enter all the numbers to be multiplied, separated by a space:\n")

    args = args.split()

    try:
        end_value = int(args[0])
        for x in args[1:]:
            end_value *= int(x)
    except ValueError:
        print("Improper value, only use numbers...")
        return times()
    print(end_value)


def div():
    args = input("Enter all the numbers to be divided, separated by a space:\n")

    args = args.split()

    try:
        end_value = int(args[0])
        for x in args[1:]:
            end_value /= int(x)
    except ValueError:
        print("Improper value, only use numbers...")
        return div()
    print(end_value)
