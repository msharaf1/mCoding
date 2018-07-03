#1.
# a = 5
# def countdown(a):
#     for i in range(a,-1, -1):
#         print([i])
# countdown(a)



""" 

def countdown(b):
    for i in range (len(b)):
        print (b[i])
countdown([5,4,3,2,1])


def countdown(b):
    for i in range (len(b)):
        print (b[i])
countdown([5,4,3,2,1])
 """

 #2.
# def printreturn(a,b):
#      print (a)
#      return (b)
# printreturn(1,3)

"""
give an array
sum of the first value, return second

arr [a, b] > a(a+b, c)
a(ab + length(c))

"""

# def arrtotal(a,b):
#     for i in range (0, (len(a+b)), i += 1):
#         a = a+b
#         b = b+ (len(a+b))
# print(6,7)
#3
""" def summarr(arr):
    sum = arr[0] + len(arr)
    print (sum)

summarr([3,8,9])

 """
#4
""" def newArr(arr):
  # newArr=[]
    for i in range(0,len(arr)):
        if i > arr[1]:
            print (arr)
        else:
            print (False)
newArr([1,2,2,6])
 """

a = 2
b =5
def lengthAndValue(a,b):
    newarr=[]
    for i in range(0,a):
        newarr.append(b)
    print (newarr)
    return (newarr)
lengthAndValue(a,b)