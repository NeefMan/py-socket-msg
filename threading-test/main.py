import threading
import random
import time

running = True
def print_random_nums(i):
    while running:
        print(f"t{i}")
        time.sleep(1)
for i in range(1, 10):
    t = threading.Thread(target=print_random_nums, args=[i])
    t.start()

print("sleeping for 5 seconds")
time.sleep(5)
print("End of sleep")
running = False