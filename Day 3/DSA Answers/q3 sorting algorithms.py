'''
3. Implementing Various Sorting Algorithms (Total 26 points)
Let's recap on the various sorting algorithms:
-	Selection sort
-	Insertion sort
-	Quick sort
-	Not covered: Bubble sort
-	Not covered: Merge sort

We will be implementing all the sorts that are covered.
a)	Implement a selection sort within a function for a list. (6 points)

Sample output:
my_list = [6, 2, 9, 7, 4, 8]
Output: [2, 4, 6, 7, 8, 9]
'''

# With reference to day 2, slide 30:
def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])
    
    return array

my_list = [6, 2, 9, 7, 4, 8]
print("Selection sort:", selectionSort(my_list, len(my_list)))


'''
b)	Implement an insertion sort within a function for a list. (6 points)
Sample output:
my_list = [6, 2, 9, 7, 4, 8]

Output: [2, 4, 6, 7, 8, 9]
'''

def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1      
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

my_list = [6, 4, 2, 9, 8, 7]
print("Insertion sort:", insertionSort(my_list))

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
'''

'''
c)	Implement an quick sort within a function for a list. (14 points)
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
