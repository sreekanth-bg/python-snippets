# Python3 program to find all pairs in 
# a list of integers with given sum 
# 
# [(3, 9), (5, 7)]
  
def findPairs(lst, K): 
    res = []
    while lst:
        num = lst.pop()                     # last element of the list
        diff = K - num                      # diff = sum - popped element 
        if diff in lst:                     # if last element + diif = sum, append last element, diff
            res.append((diff, num))         
          
    #res.reverse()
    return res
      
# Driver code
if __name__ == '__main__':
    lst = [1, 5, 3, 7, 9]
    K = 12
    print(findPairs(lst, K))
