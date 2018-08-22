#1

year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(' leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')

#2
length=int(input("enter the length :"))
breadth=int(input("enter the breadth :"))
if(length==breadth):
    print('it is a square')
else:
    print('it is a rectangle')

#3
n=int(input("enter the number of people"))
a=[]
for i in range (n):
    a.append(input('enter the age'))
    
o=max(a)
y=min(a)
print('the oldest is {} and youngest is{}'.format(o,y))

#4
age=int(input('enter age :'))
sex=input('enter sex m or f :')
martial=input('enter martial y or n :')
if(age<20 or age>60):
    print('ERROR')
else:
    if(sex=='f' or sex=='F'):
        print('work only in urban area')
    if(sex=='m' or sex=='M' and age>20 and age<40):
        print('work anywhere')
    elif(sex=='m' and age>40 and age<60):
        print('work urban areas')

  
#5
unit=int(input("enter unit that are purchased by user :"))
total=unit*100
if (total>1000):
    discount=(total*10)//100
    final=total-discount
    print('the total cost is',final)
else:
    print('the total cost is ',total)

#loops
#1
b=[]
for i in range (1,10):
    a=int(input("enter"))
    b.append(a)
for i in b:
    print(i)

#2
while True:
    print('python')
#3
n=int(input("enter"))
a=[]
c=[]
for i in range(1,n+1):
    b=int(input("enter"))
    a.append(b)
for i in a:
    d=i**2
    c.append(d)
print(c)
#4
a=int(input("enter a"))
b=int(input("enter b"))

def fun(b):
    
    if(b==0):
        return 1
    else:
        return a*fun(b-1)
    
print(fun(b))
