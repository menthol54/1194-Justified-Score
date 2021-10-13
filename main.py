import random
import calc as c
import time

greet = ["Hello. My name is 1194 Justified Score", "1194 online"]
print(random.choice(greet))
time.sleep(0.5)

def func():
    ask = input("What function would you like to access? ")
    #----------Math Funcs--------#
    if ask == 'math':
        m_func = input("What operation? ")
        if m_func == 'add':
            c.add()
        elif m_func == 'sub':
            c.sub()
        elif m_func == 'mul' or 'times':
            c.times()
        elif m_func == 'div':
            c.div()
        elif m_func == 'sqrt':
            c.rad()
    if ask == 'help':
        req = input("""
Please be more specific? Help math? Help science? 
Please say 'help' beside the subject.
Subjects: Math.
Tpye nothing to return """)
        if req == '':
            return ask
        
        elif req == 'help math':
            print('ok')

def main():
    func()
main()