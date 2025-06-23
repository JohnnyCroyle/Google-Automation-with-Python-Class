# The binary_search function returns the position of key in the list if found, or -1 if not found. 
# Add commands to print out "Checking the left side" or "Checking the right side" in the appropriate places.

def binary_search(list, key):
    """
    Searches for a key in a sorted list using binary search.

    Args:
        list: The sorted list to search.
        key: The value to search for.

    Returns:
        The index of the key in the list, or -1 if not found.
    """
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == key:
            return mid
        elif list[mid] < key:
            print("Checking the right side")
            low = mid + 1
        else:
            print("Checking the left side")
            high = mid - 1
    return -1

print(binary_search([10, 2, 9, 6, 7, 1, 5, 3, 4, 8], 1))
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(binary_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
print(binary_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
print(binary_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))