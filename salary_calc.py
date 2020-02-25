
'''
print the month of the cumulative salary
Ex:
2 -> inputs denotes 2 salaries
100 -> nput dentes intial salary 2500 -> input denotes cumulative salary
100 -> nput dentes intial salary 200 -> input denotes cumulative salary
output
1 - denotes 25th month
2 - denotes 2nd month
'''

n = int(input("Enter number of elements : "))

a = []

for i in range(0, n):
    a.append((input("\nEnter the numbers : ").strip().split()))

for i in range(0, n):
    month = int(a[i][1]) / int(a[i][0])
    def calc_month(month): return month % 12
    print(calc_month(round(month)))
