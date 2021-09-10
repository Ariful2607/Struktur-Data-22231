class persegi_panjang:
    titiksudut = 4
    
    def __init__(self, panjang=0, lebar=0): 
        self.panjang = panjang
        self.lebar = lebar
        
    def ubahukuran(self, rasio): 
        self.panjang = self.panjang * rasio
        self.lebar = self.lebar * rasio
        
    def hitungluas(self): 
        luas = self.lebar * self.panjang         
        return luas

    def hitungkeliling(self): 
        return 2*(self.lebar + self.panjang)