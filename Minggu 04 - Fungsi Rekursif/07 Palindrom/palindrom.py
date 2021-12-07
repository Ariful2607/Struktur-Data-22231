def palindrom(num=[]) :
    if len(num) == 0 :
        return True
    else:
        if num[0] == num[-1] :
            return palindrom(num[1:-1])
        else :
            return False
print (palindrom([1,2,3,4,4,3,2,1]))