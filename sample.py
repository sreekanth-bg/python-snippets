'''
2       -> N
1 2     -> num1
2 3     -> num2
[1, 2, 2, 3] [1, 2, 2, 3]
'''

N =int(input())

#input = sys.argv[1]
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

sumArray = []

for i in range(0,N):
    sumArray.append(num1+num2)

for element in sumArray:
    print(element, end=" ")

print("")

