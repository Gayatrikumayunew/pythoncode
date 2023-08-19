import time
initial = time.time()
k = 0
"""how much time while loop took"""
while(k <= 45):
    print("this")
    k += 1


print("while loop", time.time()-initial, "seconds")

