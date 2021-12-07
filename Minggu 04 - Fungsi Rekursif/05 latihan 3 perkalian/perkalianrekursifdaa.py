import time
start_time = time.time()
def perkalianrekursif(a, b):
    if a == 1:
        return b
    else:
        return b + perkalianrekursif(a-1, b)
    
print (perkalianrekursif(123, 10))
print("--- %s seconds ---" % (time.time() - start_time))

print (perkalianrekursif(10, 123))
print("--- %s seconds ---" % (time.time() - start_time))