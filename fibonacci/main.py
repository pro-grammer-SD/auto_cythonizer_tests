import time
import _fib_func as fib

start = time.time()
print(fib.fib(40))
end = time.time()

print("Time:", end - start)
