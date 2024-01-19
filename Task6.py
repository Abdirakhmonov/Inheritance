class Cars:
    def __init__(self, id, first_name, last_name, gender, brand, year, color, country):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.brand = brand
        self.year = year
        self.color = color
        self.country = country

    def gender1(self):
        erkaklar_soni = sum(1 for car in cars_list if car.gender == "erkak")
        ayollar_soni = sum(1 for car in cars_list if car.gender == "ayol")
        
        erkaklar_foiz = (erkaklar_soni / (erkaklar_soni + ayollar_soni)) * 100
        ayollar_foiz = (ayollar_soni / (erkaklar_soni + ayollar_soni)) * 100

        return f"Erkaklar foizi: {erkaklar_foiz}%, Ayollar foizi: {ayollar_foiz}%"

    def top_brand(self):
        brendlar_soni = {}
        for car in cars_list:
            brend = car.brand
            brendlar_soni[brend] = brendlar_soni.get(brend, 0) + 1

        eng_kop_brend = max(brendlar_soni, key=brendlar_soni.get)
        kam_brend = min(brendlar_soni, key=brendlar_soni.get)

        return f"Eng ko'p mashina sotilgan brend: {eng_kop_brend}, Eng kam mashina sotilgan brend: {kam_brend}"

    def prepare_letter(self):
        if self.year < 2005:
            return f"Kimdan: Auto Test Corp\nKimga: {self.first_name} {self.last_name}\nJoriy davlat: {self.country}\nHurmatli {self.first_name} {self.last_name}! {self.brand} tomonidan {self.year}da ishlab chiqarilgan {self.color} rangli avtoulovingiz Texnik holatini tekshirtirish maqsadida mahalliy Auto Test Corp. ofisiga murojaat qilishingizni so'raymiz."

cars_list = [
    Cars(1, "Eshmat", "Toshmatov", "erkak", "Toyota", 2002, "qora", "Uzbekistan"),
    Cars(2, "Toshmat", "Eshmatov", "ayol", "Toyota", 2005, "oq", "Kyrgyzstan"),
    Cars(3, "Sardor", "Mirzaev", "erkak", "Honda", 2003, "ko'k", "Kazakhstan"),
]

print(cars_list[0].gender1())

print(cars_list[0].top_brand())


for car in cars_list:
    if car.year < 2005:
        print(car.prepare_letter())
