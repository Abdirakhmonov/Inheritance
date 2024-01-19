class Transport:
    def __init__(self, brand, model, color) -> None:
        self.brand = brand
        self.model = model
        self.color = color

    def getInfo(self):
        return f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}"
    
    def setBrand(self, new_brand):
        self.brand = new_brand
    
    def setModel(self, new_model):
        self.model = new_model
    
    def setColor(self, new_color):
        self.color = new_color
    
class Car(Transport):
    def __init__(self, brand, model, color, speed, seatCount, manifactureDate) -> None:
        super().__init__(brand, model, color)
        self.speed = speed
        self.seatCount = seatCount
        self.manifactureDate = manifactureDate

    def getInfo(self):
        trans_info = super().getInfo()
        return f"{trans_info}, Speed: {self.speed}, SeatCount: {self.seatCount}, ManifactureDate: {self.manifactureDate}"

    def SetSpeed(self, new_speed):
        self.speed = new_speed
    
    def SetseatCount(self, new_seatcount):
        self.seatCount = new_seatcount
    
    def SetManifactureDate(self, new_manifactureDate):
        self.manifactureDate = new_manifactureDate
    
class Truck(Transport):
    def __init__(self, brand, model, color, weightcapacity) -> None:
        super().__init__(brand, model, color)
        self.weightcapacity = weightcapacity
    
    def getInfo(self):
        trans_info = super().getInfo()
        return f"{trans_info}, Weight Capacity: {self.weightcapacity}"

    def SetWeightCapacity(self, weight_capacity):
        self.weightcapacity = weight_capacity



car = Car("Toyota", "Camry", "Blue", 120, 5, "2022-01-01")
print(car.getInfo())

truck = Truck("Volvo", "VNL", "Red", 5000)
print(truck.getInfo())


