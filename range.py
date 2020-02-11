'''
print range of integers after getting start an end from user)
python range.py 
5,9
5 6 7 8 9 
'''

# Below line read inputs from user using map() function 
a,b = map(int,input().strip().split(','))

for n in range(a,b+1):
    print(n,end =" ")