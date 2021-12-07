def faktorialnonrekursif(bil):
    hasil = 1
    for i in range(1, bil+1):
        hasil = hasil*i
    return hasil
    
print (faktorialnonrekursif(5))
print (faktorialnonrekursif(6))
print (faktorialnonrekursif(7))

print (faktorialnonrekursif(0))