# Лабораторная работа №3 ====================================================================================================

# 1) Singleton (Одиночка) ---------------------------------------------------------------------------------------------------

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Car(metaclass=SingletonMeta):
    def __init__(self, model: str):
        self.model = model
        self.speed = 0

    def accelerate(self, delta: int):
        self.speed += delta
        print(f"{self.model} ускоряется. Текущая скорость: {self.speed} км/ч")
        
    def stop(self):
        self.speed = 0
        print(f"{self.model} остановилась.")

print("\n===================== 1) Singleton (Одиночка) =====================\n")
car1 = Car("Mazda Capella")
car2 = Car("Toyota Camry")

print(car1 is car2) # True
car1.accelerate(50)
car2.accelerate(30)
print(f"Модель: {car1.model}, скорость: {car1.speed} км/ч")
print(f"Модель: {car2.model}, скорость: {car2.speed} км/ч")





# 2) Factory Method (Фабричный метод) ---------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def zavesti(self):
        pass

class Gruzovik(Transport):
    def zavesti(self):
        return "Грузовик заведён"

class Auto(Transport):
    def zavesti(self):
        return "Машина заведена"


class Dist_zapusk(ABC):
    @abstractmethod
    def zapusk(self):
        pass

class Dist_gruzovik(Dist_zapusk):
    def zapusk(self):
        return Gruzovik()

class Dist_auto(Dist_zapusk):
    def zapusk(self):
        return Auto()


dist = Dist_auto()
auto = dist.zapusk()
print("\n===================== 2) Factory Method (Фабричный метод) =====================\n")
print(auto.zavesti())




# 3) Abstract factory (Абстрактная фабрика) ---------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Абстрактные продукты
class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Bike(ABC):
    @abstractmethod
    def ride(self):
        pass


# Конкретные продукты
class MazdaCar(Car):
    def drive(self):
        return "Driving Masda car"

class MazdaBike(Bike):
    def ride(self):
        return "Riding Mazda bike"

class ToyotaCar(Car):
    def drive(self):
        return "Driving Toyota car"

class ToyotaBike(Bike):
    def ride(self):
        return "Riding Toyota bike"

# Абстрактная фабрика
class TransportFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass
    
    @abstractmethod
    def create_bike(self) -> Bike:
        pass


# Конкретные фабрики
class MazdaFactory(TransportFactory):
    def create_car(self) -> Car:
        return MazdaCar()
    
    def create_bike(self) -> Bike:
        return MazdaBike()

class ToyotaFactory(TransportFactory):
    def create_car(self) -> Car:
        return ToyotaCar()
    
    def create_bike(self) -> Bike:
        return ToyotaBike()


print("\n===================== 3) Abstract factory (Абстрактная фабрика) =====================\n")
# Использование
def client_code(factory: TransportFactory):
    car = factory.create_car()
    bike = factory.create_bike()
    print(car.drive())
    print(bike.ride())

print("Mazda:")
client_code(MazdaFactory())
print("Toyota:")
client_code(ToyotaFactory())





# 4) Builder (Строитель) ----------------------------------------------------------------------------------------------------

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def __str__(self):
        return f"CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB"

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def build(self):
        return self.computer

builder = ComputerBuilder()
pc = builder.set_cpu("Intel i5").set_ram(16).set_storage(512).build()
print("\n===================== 4) Builder (Строитель) =====================\n")
print(pc)
print("\n--------------------------------------------------------------------")


