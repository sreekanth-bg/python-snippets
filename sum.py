'''
print sum of integers in an array of size N (users inputs integers sperated by ',')
'''

# number of elements 
n = int(input("Enter number of elements : ")) 

# Below line read inputs from user using map() function 
a = list(map(int,input("\nEnter the numbers : ").strip().split(',')))[:n] 

print("\nList is - ", a) 

print("\nSum is - {0}".format(sum(a)))