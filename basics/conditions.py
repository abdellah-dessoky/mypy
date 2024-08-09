msg ='123'
inputMsg = input('please enter a msg :')
# comparison operator 
if inputMsg == msg:
    print("done")
else:
    print('wrong msg')
x =12
y = int(input('Enter a number :'))
if x>y:
    print('1st condition')
    print('x is greater than y')
if x<y:
    print('2nd condition')
    print('y is smaller than x')
# logical operator 
if not (x>y):
    print('3rd condition')
    print('x not greater than y')
if not (x<y):
    print('4th condition')
    print('y not greater than x')
if x!=y :
    print('5th condition')
    print('not equal y')
if x is y:
    print('6th condition')
    print('they are integers')
if x == y:
    print('7th condition')
    print('x and y are equal')
if x==y and y==x:
    #random useless if just practicing 
    print('8th cond')
    print('x is greater than or equal to y')
if x==y or x>=y:
    print('9th cond')
    print('x is greater than or equal to y')


    
"""comment section
- not (x==y) which means x not equal to y, not (x<y) which means x greater than y, not (x>y) which means y greater than x
- is which checks if the share the same memory address 
- is not which means the opposite of it 
- comparison operators <= ,>= greater than or equal and smaller than or equal
- int(input(Enter a number)) input method does return a string and int method does convert it to int 
- and,or,and not are the logical operators for python
- 

"""