'''
print sum of array by following pattern of A[i] replacing with A[i] + A[i+1]
Ex:
3 ->
1 2 3 -> input
3 5 -> becomes in next step
8 -> output
'''


def new_list(a):
    b = []
    length = len(a)
    for i in range(0, length-1):
        b.append(a[i]+a[i+1])
    return(b) if len(b) == 1 else new_list(b)


# number of elements
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

sum = new_list(a)

print(*sum, sep=", ")
