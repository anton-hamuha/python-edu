def fibonacci_generater():
    a = b = 1
    while true:
        yield a
        a, b = b, a + b
fib = fibonacci_generater()
for i in fib:
    if i > 100:
        break
    else:
        print('generated:', i)
