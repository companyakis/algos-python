# log(n)

def big_o_log_n(n):
    import math
    while n > 1:
        n = math.floor(n / 2)
        print (n)
        
big_o_log_n(8)

big_o_log_n(50)
    

# 4 
# 2 
# 1 

# 25
# 12
# 6 
# 3 
# 1 


