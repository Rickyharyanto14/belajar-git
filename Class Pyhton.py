class Orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print(f"perkenalan nama saya {self.nama} dari {self.asal}")
    
    def pergi(self):
        print(f"{self.nama} pulang ke {self.asal}")
   
    
andi = Orang('Andi','Surabaya')
andi.perkenalan()
