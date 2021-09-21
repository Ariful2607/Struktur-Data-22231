import ctypes
class Array :
    def __init__(self,ukuran):
        assert ukuran > 0, "array harus memiliki elemen sebanyak > 0"
        self.ukuran = ukuran
        PyArrayType = ctypes.py_object * ukuran
        self.anggota = PyArrayType()

    def getlength(self):
        return self.ukuran

    def getitem(self,index):
        assert index >= 0
        return self.anggota[index]

    def setitem(self,index,value):
        assert index >= 0
        self.anggota[index] = value

    def clear(self,value):
        for i in range( getlength(self) ) :
           self.anggota[i] = value

#Buat array dengan index 5
arr = Array(5)

#Set item seluruh index array dengan nilai 5
for i in range(arr.ukuran):
    arr.setitem(i,5)

#Set item index 1 dan 3 dengan nilai 8 dan 10
arr.setitem(1,8)
arr.setitem(3,10)

# #Cetak array index ke 1,2,3
print (arr.getitem(1))
print (arr.getitem(2))
print (arr.getitem(3))

# #Cetak nilai semua index
# for i in range (arr.ukuran):
#     print ("index",i," adalah :", arr.getitem(i))