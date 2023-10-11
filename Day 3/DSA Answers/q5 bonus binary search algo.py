'''
Bonus: Implementing Binary Search on a List (Total 5 points)

In this exercise, we will define a function to search whether a 
number exists in a list, using a binary search algorithm. 
The return value is Boolean. You are allowed to search up on this.

Bonus content (optional):
	Binary Search, O(log_2 n) = O(log n)
	Sequential Search, or linear search, O(n)
'''

def binary_search(list, search_value):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        middle = (first + last)//2 # Floor division means to round down the 
        # division. 
        # Check whether the search value equals the value in the middle
        if search_value == list[middle]:
            return True
            # Check whether the search value is smaller than the value in the middle
        elif search_value < list[middle]:
            # Set last to the value of middle minus one
            last = middle - 1
        else:
            first = middle + 1
    return False
    
print(binary_search([1,5,8,9,15,16,70,71], 5))
print(binary_search([1,5,8,9,15,16,70,71], 67))