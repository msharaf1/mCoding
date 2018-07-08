#1
""" def biggieSize(arr):
    for i in range(0,len(arr)):
        if arr[i] > 0:
            arr[i] = "Biggie"
    print (arr)

biggieSize([-3,-2,-1,3,4,5,7])

 """

 #2.

""" 
def countPositive(arr):
    count = 0
    for i in range(len(arr)):
         if arr[i] >0:
            count +=1
    arr[len(arr)-1] = count
    return arr

print(countPositive([-1,-2,1,2,1])) """

#3. 

# def sumArr(arr):
#     sum =0
#     for i in range(len(arr)):
#         sum = arr[i]+ sum
#     return sum
# print(sumArr([1,3,4,2]))
""" 
def sumArr(arr):
    sum =0
    for i in arr:
        sum += i
    return sum
print(sumArr([1,3,4,2]))

 """

# list = ["John", "Khan", "Jaan"]
# if "Jaan" in list:
#      print("Yay")


## print the numbers from 0 through 99
# for i in range(100):
#     print (i)
""" 
def sumArr(arr):
    sum =0
    for i in range(len(arr)):
        sum = arr[i]+ sum
        avg = sum/len(arr)
    #return sum / len(arr)
    return avg
print(sumArr([1,3,4,2]))
 """
#5.
""" def countLength(arr):
    count = 0
    for i in range(len(arr)):
        count = i
    return count
print(countLength([2,3,4,5,8]))

 """
#6.
""" 
def minArr(arr):
    
    if len(arr) == "":
        return False
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min
print(minArr([2,-4,5,8, 482, 112, -9, 13, 3, 1]))
#print(minArr([2,-4,5,8]))
 """
 #7
def maxValue(arr):
    if len(arr) == "":
        return False
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
print(maxValue([34,2,6,500,20,-3,-1]))

