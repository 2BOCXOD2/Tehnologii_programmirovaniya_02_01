from abc import ABC, abstractmethod

# Базовый класс для всех игровых объектов
class GameObject(ABC):
    def __init__(self, id, name, x, y):
        self._id = id
        self._name = name
        self._x = x
        self._y = y

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y


# Интерфейс для атакующих объектов
class Attacker(ABC):
    @abstractmethod
    def attack(self, unit):
        pass

# Интерфейс для перемещаемых объектов
class Moveable(ABC):
    @abstractmethod
    def move(self, x, y):
        pass

# Класс юнита
class Unit(GameObject):
    def __init__(self, id, name, x, y, hp):
        super().__init__(id, name, x, y)
        self._hp = hp

    def is_alive(self):
        return self._hp > 0

    def get_hp(self):
        return self._hp

    def receive_damage(self, damage):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0

# Класс лучника
class Archer(Unit, Moveable, Attacker):
    def __init__(self, id, name, x, y, hp, attack_power):
        super().__init__(id, name, x, y, hp)
        self._attack_power = attack_power

    def attack(self, unit):
        if unit.is_alive:
            unit.receive_damage(self._attack_power)
            print(f"{self.get_name()} атакует {unit.get_name()} и наносит {self._attack_power} урона.")
        else:
            print(f"{self.get_name()} не может атаковать")

    def move(self, x, y):
        self._x = x
        self._y = y
        print(f"{self.get_name()} переместился в новую точку с координатами: x={x}, y={y}")

# Класс постройки
class Building(GameObject):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y)
        self._built = built

    def is_built(self):
        return self._built

# Класс крепости
class Fort(Building, Attacker):
    def __init__(self, id, name, x, y, built, attack_power, hp):
        super().__init__(id, name, x, y, built)
        self._attack_power = attack_power
        self._hp = hp

    def attack(self, unit):
        if unit.is_alive():
            unit.receive_damage(self._attack_power)
            print(f"{self.get_name()} атакует {unit.get_name()} и наносит {self._attack_power} урона.")
        else:
            print(f"{self.get_name()} не может атаковать")

    def is_alive(self):
        return True # Крепость всегда "жива"

    def receive_damage(self, damage):
        # Здесь можно добавить логику для уменьшения прочности крепости
        print(f"{self.get_name()} получает {damage} урона.")

    def get_hp(self):
        return self._hp

# Класс мобильного дома
class MobileHome(Building, Moveable):
    def __init__(self, id, name, x, y, built):
        super().__init__(id, name, x, y, built)

    def move(self, x, y):
        self._x = x
        self._y = y
        print(f"{self.get_name()} переместился в новую точку с координатами: x={x}, y={y}")



# ТЕСТ
archer = Archer(1, "Лучник", 0, 0, 100, 10)
fort = Fort(2, "Крепость", 5, 5, True, 20, 100)
mobile_home = MobileHome(3, "Мобильный дом", 10, 10, False)
archer.move(3, 3)
archer.attack(fort)
fort.attack(archer)
print(f"Здоровье лучника: {archer.get_hp()}")
print(f"Здоровье крепости: {fort.get_hp()}")

# cd labs/lab_02
# python klassy.py