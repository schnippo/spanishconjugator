def fib(max):
    a = 1
    b = 1
    for i in range(max):
        old_a = a
        a += b
        b = old_a
        print(a)
fib(100)