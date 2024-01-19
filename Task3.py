class Countries:
    def __init__(self, davlat_nomi, poytahti, aholi_soni, yer_maydoni, prezidenti) -> None:
        self.davlat_nomi = davlat_nomi
        self.poytahti = poytahti
        self.aholi_soni = aholi_soni
        self.yer_maydoni = yer_maydoni
        self.prezidenti = prezidenti
        
    def info(self):
        return f"Davlat nomi: {self.davlat_nomi}, Poytahti: {self.poytahti}, Aholi soni: {self.aholi_soni}, Yer maydoni: {self.yer_maydoni}, Prezidenti: {self.prezidenti}"
    
davlatlar = [
    Countries("Uzbekistan", "Tashkent", 36_000_000, 300_000, "Mirziyoyev"),
    Countries("Kyrgyzstan", "Bishkek", 7_000_000, 195_000, "Japarov"),
    Countries("Tajikistan", "Dushanbe", 10_000_000, 200_000, "Rahmonov"),
    Countries("Turkey", "Istambul", 136_000_000, 300_000, "Erdog'an"),
    Countries("Amerika", "New-York", 236_000_000, 300_000, "Bayden")
]
davlatlar.sort(key=lambda x: x.davlat_nomi)

for davlat in davlatlar:
    print(davlat.info())