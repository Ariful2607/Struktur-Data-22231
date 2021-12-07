def cariterbesar(bil1, bil2, bil3):
    terbesar = 0
    if bil1 > bil2:
        terbesar = bil1
    else:
        terbesar = bil2
    if bil3 > terbesar:
        terbesar = bil3
    return terbesar

print (cariterbesar(3, 1, 5))
print (cariterbesar(1, 1, 7))
print (cariterbesar(4, 4, 2))