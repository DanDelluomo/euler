import time
t0 = time.time()
def fib_gen():
    fibs = [1, 1]
    next_fib = 0
    while len(str(next_fib)) < 1000:
        next_fib = fibs[-1] + fibs[-2]
        fibs.append(next_fib)
        if len(str(next_fib)) == 1000:
            return len(fibs)

print(fib_gen())
t1 = time.time()
total = t1-t0
print(total)
