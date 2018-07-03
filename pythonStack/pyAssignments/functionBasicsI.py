#1
def a():
    return 5
print(a())

#5
#this prints 5. 

#2
def a():
    return 5
print(a()+a())

#it should print 10.
#10

#3

def a():
    return 5
    return 10
print(a())
#5
#it should print 5 and escape 10.

#4
def a():
    return 5
    print(10)
print(a())
#5
#5

def a():
    print(5)
x = a()
print(x) #there is no argument passed

#6
""" def a(b,c):
    print(b+c)
print(a(1,2)+a(2,3))
 """
#error

#7

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#Take integer, but prints it as string.

#8
""" 
def a():
    b=100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)
 """

#9:

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 4
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#11:

def a(b,c):
    return b+c
    return 10
print(a(3,5))

#12:

b=500
print(b)
def a():
    b=300
    print(b)
print(b)
a()
print(b)
#500, 500, 300, 500
x="Hello"
print (x)


b=500
print(b)
def a():
    b=300
    print(b)
    return b
print(b)
a()
print(b)

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

##