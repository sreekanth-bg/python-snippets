# Creating a bubble sort function  
def bubble_sort(list1):  
    # Outer loop for traverse the entire list  
    for i in range(len(list1)-1):  
        for j in range(len(list1)-1):  
            if(list1[j]>list1[j+1]):  
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1  
  
list1 = [64, 34, 25, 12, 22, 11, 90]  
print("The unsorted list is: ", list1)  
# Calling the bubble sort function  
print("The sorted list is: ", bubble_sort(list1))  
# [64, 34, 25, 12, 22, 11, 90]