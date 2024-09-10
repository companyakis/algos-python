# n log(n)

def n_log_n(n):
    import math
    coef = n
    while n > 1:
        n = math.floor(n / 2)
        for i in range(1, coef):
            print(i)


n_log_n(4)
