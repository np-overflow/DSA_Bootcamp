'''
4. Implementing Various Sorting Algorithms (Total 26 points)
Let's recap on the various sorting algorithms:
-	Selection sort
-	Insertion sort
-	Quick sort
-	Bonus: Bubble sort
-	Bonus: Merge sort

We will be implementing all the sorts that are covered.
a)	Implement a selection sort within a function for a list.

Sample output:
my_list = [6, 2, 9, 7, 4, 8]
Output: [2, 4, 6, 7, 8, 9]
'''

def selection_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        # Set lowest to the index of the current element
        lowest = i
        # Iterate again over the list starting on the next position of the i variable
        for j in range(i + 1, list_length):
            # Compare whether the element of the list located at index j is smaller than the current lowest
            if my_list[j] < my_list[lowest]:
                lowest = j
        # Swap the current element with the lowest element found
        my_list[i], my_list[lowest] = my_list[lowest], my_list[i]
    return my_list

my_list = [6, 2, 9, 7, 4, 8]
print("Selection sort:", selection_sort(my_list))


'''
b)	Implement an insertion sort within a function for a list.
Sample output:
my_list = [6, 2, 9, 7, 4, 8]

Output: [2, 4, 6, 7, 8, 9]
'''

def insertion_sort(my_list):
    list_length = len(my_list)
    for i in range(1, list_length):
        current_no = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > current_no:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = current_no
    return my_list

my_list = [6, 4, 2, 9, 8, 7]
print("Insertion sort:", insertion_sort(my_list))



'''
c)	Implement an insertion sort within a function for a list.
Sample output:
arr = [4, 6, 2, 7, 1, 9, 5]

Output: [1, 2, 4, 5, 6, 7, 9]
'''

def quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr = [4, 6, 2, 7, 1, 9, 5]
quick_sort(arr)
print("Quick sort:", arr)
