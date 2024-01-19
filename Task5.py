class Soldat:
    def __init__(self, yoshi: int, jinsi: str, boyi: float, vazni: int) -> None:
        self.yoshi = yoshi
        self.jinsi = jinsi
        self.boyi = boyi
        self.vazni = vazni


class Armiya(Soldat):
    def habar(self):
        if self.yoshi > 18 and self.jinsi == "erkak":
            if self.boyi < 150 and self.vazni < 75:
                return "Piyoda askarligiga"
            else:
                return "Tank qo'shinlariga"
            

soldat = Soldat(21, "erkak", 176.5, 65)
armiya = Armiya(21, "erkak", 176.5, 65)

habar = armiya.habar()

print(f"Siz malumotlarini kiritgan soldat {habar} yo'naltirildi!")
       