# TODO The find_item function uses binary search to recursively locate an item in a list, returning True if found, False otherwise. The function assumes the list is sorted; make sure to sort the list before calling this function. Add debug lines where appropriate to help you narrow down the problem.

def find_item(listed, item):
    """
    Uses binary search to recursively locate an item in a list.

    Args:
        listed: The sorted list to search.
        item: The item to search for.

    Returns:
        True if the item is found, False otherwise.
    """
    print(f"Searching for {item} in {listed}") # Debug line 1
    if not listed:
        print("List is empty") # Debug line 2
        return False

    mid = len(listed) // 2
    print(f"Middle index: {mid}, Middle item: {listed[mid]}") # Debug line 3

    if listed[mid] == item:
        print("Item found!") # Debug line 4
        return True
    elif item < listed[mid]:
        print("Searching in the left half") # Debug line 5
        return find_item(listed[:mid], item)
    else:
        print("Searching in the right half") # Debug line 6
        return find_item(listed[mid+1:], item)


#Do not edit below this line - This code helps check your work!
list_of_names = ["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"]

# Sort the list before searching
list_of_names.sort()

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False