import time
t = time.time()
m = 0
for i in range(10000000):
        m += 1

print(time.time() - t)
