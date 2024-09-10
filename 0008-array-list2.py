def memory_usage(n: int):
    import sys 
    
    dynamic_array = []
    
    for i in range(n):
        len_arr = len(dynamic_array)
        byte_arr = sys.getsizeof(dynamic_array)
        print(f"Array length: {len_arr} and byte: {byte_arr}")
        dynamic_array.append(i)
        #print(dynamic_array)
        
memory_usage(20)

# Array length: 0 and byte: 56 
# Array length: 1 and byte: 88 
# Array length: 2 and byte: 88 
# Array length: 3 and byte: 88 
# Array length: 4 and byte: 88 
# Array length: 5 and byte: 120
# Array length: 6 and byte: 120
# Array length: 7 and byte: 120
# Array length: 8 and byte: 120
# Array length: 9 and byte: 184
# Array length: 10 and byte: 184
# Array length: 11 and byte: 184
# Array length: 12 and byte: 184
# Array length: 13 and byte: 184
# Array length: 14 and byte: 184
# Array length: 15 and byte: 184
# Array length: 16 and byte: 184
# Array length: 17 and byte: 248
# Array length: 18 and byte: 248
# Array length: 19 and byte: 248
