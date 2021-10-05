import ctypes
class Array :
    def __init__(self,ukuran):
        assert ukuran > 0, "array harus memiliki elemen sebanyak > 0"
        self.ukuran = ukuran
        PyArrayType = ctypes.py_object * ukuran
        self.anggota = PyArrayType()
        self.Max = 0
        self.Min = 0

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

    def getmax(self):
        for i in self.anggota:
            if i > self.Max:
                self.Max=i
        return self.Max
    
    def getmin(self):
        self.Min = self.anggota[0]
        for i in self.anggota:
            if i < self.Min:
                self.Min=i
        return self.Min

    def getselisih(self):
        return self.Max-self.Min

#Buatlah array berkuran 10
arr = Array(10)


#Setlah semua data di array yang anda buat dengan nilai 10
for i in range(arr.ukuran):
    arr.setitem(i,10)


#Cetaklah seluruh array
# for i in range(arr.ukuran):
#     print ("index",i," adalah :", arr.getitem(i))

#Isilah elemen ke 2 dengan 8, elemen 4 dengan 100, elemen 0 dengan 50
arr.setitem(1,8)
arr.setitem(3,100)
arr.setitem(0,50)

# 50  8   10  100 10  10  10  10  10  10
# 0   1   2   3   4   5   6   7   8   9

#Cetak array index ke 1,2,3
# print (arr.getitem(1))
# print (arr.getitem(2))
# print (arr.getitem(3))

#Cetak nilai semua index yang telah di set
# for i in range (arr.ukuran):
#     print ("index",i," adalah :", arr.getitem(i))

#Tambahkan function getMax() untuk mencari nilai terbesar di array tersebut.
print (arr.getmax())
print (arr.getmin())

#Buat function mencari range (selisih bilangan terbesar dengan terkecil).
print (arr.getselisih())