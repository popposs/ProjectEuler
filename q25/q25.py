def fibo():
    array = [1, 1]
    next_fib = 1 # placeholder
    index = 2

    while len(str(next_fib)) != 1000:
        index += 1
        next_fib = array[0] + array[1]
        array[0], array[1] = array[1], next_fib

    print index 
fibo()
    
