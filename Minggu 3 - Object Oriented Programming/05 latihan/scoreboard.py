class scoreboard:

    def __init__(self, tim1, tim2, skor1=0, skor2=0):
        self.tim1 = tim1
        self.tim2 = tim2
        self.skor1 = skor1
        self.skor2 = skor2

    def reset(self):
        self.skor1 = 0
        self.skor2 = 0

    def up1(self):
        self.skor1 += 1

    def up2(self):
        self.skor2 += 1

    def down1(self):
        self.skor1 -= 1

    def down2(self):
        self.skor2 -= 1

    def peek1(self):
        return self.skor1

    def peek2(self):
        return self.skor2
