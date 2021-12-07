def faktorialrekursif(bil):
    if bil <= 1:
        return 1
    else:
        return bil * faktorialrekursif(bil - 1)

print (faktorialrekursif(5))
print (faktorialrekursif(6))
print (faktorialrekursif(7))

print (faktorialrekursif(0))