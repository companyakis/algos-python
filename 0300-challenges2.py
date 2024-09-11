# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
A	B	XOR

0	0	0

0	1	1

1	0	1

1	1	0

"""

def find_unique_item(l: list[int]) -> int:
    result = 0
    
    for i in l:
        result = i ^ result
        
    return result

l1 = [9, 8, 7, 6, 7, 9, 8]

print("Unique item: ", find_unique_item(l1)) # Unique item: 6
