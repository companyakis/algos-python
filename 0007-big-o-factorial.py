def big_o_factorial(n: int):
    
    if n == 0:
        print(1)
    else:
        for i in range(n):
            print(i)
            big_o_factorial(n - 1)
    

big_o_factorial(5)
