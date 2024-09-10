# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def duplicated(l: list[int]):
    
    if len(l) != len(set(l)):
        return True
    return False


l0 = [0, 2, 4, 6, 8, 11, 47, 987, 9999, 2000, 2]

print(duplicated(l0)) # True
    
l1 = [22, 45, 87, 92, 21, 100]

print(duplicated(l1)) # False

l2 = [22, 45, 87, 92, 21, 100, -5000, 240, 101, 92]
    
print(duplicated(l2)) # True     

