class Mashina:
    def __init__(self, m_nomi, m_turi, yili, m_narhi = 4000):
        self.m_nomi = m_nomi
        self.turi = m_turi
        self.narhi = m_narhi
        self.yili = yili
    def info(self):
        return f"Nomi: {self.m_nomi}, Turi(yuk/yengil): {self.turi}, Narhi: {self.narhi}$, Yili: {self.yili}\n"
mashinalar = [
    Mashina("Toyota", "yengil", 2022, 25000),
    Mashina("Honda", "yengil", 2018),
    Mashina("Ford", "yuk avtomobili", 2015, 35000),
    Mashina("Chevrolet", "yuk avtomobili", 2023, 30000),
    Mashina("Nissan", "yengil", 2019),
    Mashina("BMW", "yengil", 2021, 40000),
    Mashina("Mercedes", "yengil", 2023, 45000),
    Mashina("Kia", "yengil", 2020),
    Mashina("Hyundai", "yengil", 2022),
    Mashina("Audi", "yengil", 2021, 42000)
]

mashinalar.sort(key=lambda x: x.yili)

for mashina in mashinalar:
    print(mashina.info())

