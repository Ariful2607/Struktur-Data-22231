def pangkatdua(n):
    if n == 0:
        return 1
    else:
        return pangkatdua(n-1) + pangkatdua(n-1)
    
print (pangkatdua(4))