#!/usr/bin/env python3
# Student ID: ekoleci
def function1():
    print('print() call in function1 on schoolName:', schoolName)

def function2():
    print('print() call in function2 on schoolName:', schoolName)

schoolName = 'Seneca College'
print('print() call in main on schoolName:', schoolName)
function1()
print('print() call in main on schoolName:', schoolName)
function2()
print('print() call in main on schoolName:', schoolName)
