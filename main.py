import random
import calc as c

greet = ["Hello. My name is 1194 Justified Score", "1194 online"]
print(random.choice(greet))

def math():
    ask = input("What function would you like to access? ")
    if ask == 'math':
        m_func = input("What operation? ")
        if m_func == 'add':
            c.add()
        if m_func == 'sub':
            c.sub()
