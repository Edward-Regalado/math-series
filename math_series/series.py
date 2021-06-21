# num = 9
def fibonacci(n):

    if n == 0:
        return 0

    elif n == 1:
        return 1
    
    return fibonacci(n-2) + fibonacci(n-1)

def lucas(n):

    if n == 0:
        return 2

    if n == 1: 
        return 1

    return lucas(n-1) + lucas(n-2)

def sum_series(n, x=0,  y=1):

   if n == 0:
       return x
   if n == 1:
       return y
   return sum_series(n - 2, x, y) + sum_series(n - 1, x, y) 