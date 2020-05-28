def sum_arr_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return sum_arr_recursion(arr[:len(arr)//2]) + sum_arr_recursion(arr[len(arr)//2:])

def sum_arr_iterative(arr):
    sum = 0
    for x in arr:
        sum += x
    return sum

def count_items_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return 1 + count_items_recursion(arr[1:])

def count_items_iterative(arr):
    count = 0
    for x in arr:
        count += 1
    return count

def find_max_recursion(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        max_tail = find_max_recursion(arr[1:])
        if arr[0] > max_tail:
            return arr[0]
        else:
            return max_tail

def find_max_iterative(arr):
    max = arr[0]
    for x in arr:
        if x > max:
            max = x
    return max

def qsort(arr):
    if len(arr) <= 1:
        # print(arr)
        return arr
    else:
        pivot = arr[0]
        smaller = []
        bigger = []
        for x in arr:
            if x < pivot:
                smaller.append(x)
            elif x > pivot:
                bigger.append(x)
        return qsort(smaller) + [pivot] + qsort(bigger)

def binary_search(arr, x):
    if len(arr) == 1 and arr[0] != x:
        return False
    middle = arr[len(arr)//2]
    if middle == x:
        return True
    elif middle < x:
        return binary_search(arr[len(arr)//2:], x)
    elif middle > x:
        return binary_search(arr[:len(arr)//2], x)
    else:
        return False

if __name__ == "__main__":
    arr = [9, 5, 3, 4, 54, 1]
    print(f'Working with array: {arr}')
    print(f'Suming the array \n \
        Should be {sum(arr)} \n \
        recursive function returned {sum_arr_recursion(arr)}\n \
        iterative function returned {sum_arr_iterative(arr)}')
    print(f'Counting items \n \
        Should be {len(arr)} \n \
        recursive function returned {count_items_recursion(arr)}\n \
        iterative function returned {count_items_iterative(arr)}')
    print(f'Finding the maximum value\n\
        Should be {max(arr)}\n\
        recursive function returned {find_max_recursion(arr)}\n \
        iterative function returned {find_max_iterative(arr)}')
    print(arr)
    print(f'Sorting the array\n\
        Should be {sorted(arr)}\n\
        quicksort returned {qsort(arr)}')
    # Sorting arrray so binary search can work
    arr.sort()
    x = int(input('What number do you want to search for? '))
    print(f'Number is in Array: {x in arr}\n \
        binary search returned {binary_search(arr, x)}')
