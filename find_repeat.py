# Python program to print
# duplicates from a list
# of integers

def Repeat(list):
    _size = len(list)
    rlist = []
    for i in range(_size):
        k = i + 1
        for j in range(k, _size):
            if list[i] == list[j] and list[i] not in rlist:
                rlist.append(x[i])
    return rlist
 
# Driver Code
list = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print (Repeat(list))
