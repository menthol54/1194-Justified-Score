import random
import calc as c
import time
import os

greet = ["Hello. My name is 1194 Justified Score", "1194 online"]
print(random.choice(greet))
time.sleep(0.5)


def func():
    #----------Math Funcs--------#
    m_func = input("What operation? ")
    if m_func == 'add':
        c.add()
    elif m_func == 'sub':
        c.sub()
    elif m_func == 'mul' or m_func == 'times':
        c.times()
    elif m_func == 'div':
        c.div()
    else:
        return func()


def main():
    func()
if __name__ == '__main__':
    main()

input('')
