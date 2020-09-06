# Function that writes the Fibonacci series to
# an arbitrary boundary 

def fib(n): # write Fibonaci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined :

fib(2000)
