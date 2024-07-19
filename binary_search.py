def binary_search(list, num):

    low = 0
    higth =len(list)-1
    while low <= higth:
        mid = low + (higth- low)//2
        
        if num == list[mid]:
            return mid
        elif num < list[mid]:
            higth =  mid - 1
        else :   
            low = mid + 1
    return None
list =[1,2,3,4,5,6,7]
num = 3
rut =binary_search(list,num)
print(rut)




def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    :param arr: List of sorted elements
    :param target: Element to search for
    :return: Index of target if found, else -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in the array")
