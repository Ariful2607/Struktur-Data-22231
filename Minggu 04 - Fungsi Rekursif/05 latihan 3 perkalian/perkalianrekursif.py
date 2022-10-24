def perkalianrekursif(bil1, bil2):
    if bil1 == 1:
        return bil2
    else:
        return perkalianrekursif(bil1-1, bil2) + bil2
    
print (perkalianrekursif(2, 3))
print (perkalianrekursif(5, 4))
print (perkalianrekursif(7, 8))