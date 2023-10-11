'''
Bonus: Implementing Binary Search on a List (Total 20 points)

The lessons have covered on searching through a tree. We can now try to implement the same principles on a list. 
In this exercise, we will define a function to search whether a number exists in a list, using a binary search algorithm. The return value is Boolean.

Bonus content (optional):
	Binary Search, O(log_2 n) = O(log n)
	Sequential Search, or linear search, O(n)
'''

def binary_search(ordered_list, search_value):
    first = 0
    last = len(ordered_list) - 1
    
    while first <= last:
        middle = (first + last)//2
        # Check whether the search value equals the value in the middle
        if search_value == ordered_list[middle]:
            return True
            # Check whether the search value is smaller than the value in the middle
        elif search_value < ordered_list[middle]:
            # Set last to the value of middle minus one
            last = middle - 1
        else:
            first = middle + 1
    return False
    
print(binary_search([1,5,8,9,15,20,70,72], 5))
