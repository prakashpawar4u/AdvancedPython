#from errno import EL


class Car:
    def __init__(self,wheels = 4):
        self.wheels = wheels

class Gasoline(Car):
    def __init__(self, engine="Gasoline",tank_cap = 20):
        Car.__init__(self)
        self.engine = engine
        self.tank_cap = tank_cap
        self.tank = 0
    
    def refuel(self):
        self.tank = self.tank_cap
class Electric(Car):
    def __init__(self, engine="Electric", kWH_cap=60):
        Car.__init__(self)
        self.engine = engine
        self.kWH_cap = kWH_cap
        self.kWH = 0
    
    def recharge(self):
        self.kWH = self.kWH_cap

class Hybrid(Gasoline, Electric):
    def __init__(self, engine="Hybrid", tank_cap=11, kWH_cap=5 ):
        Gasoline.__init__(self,engine,tank_cap)
        Electric.__init__(self,engine,kWH_cap)

Nexon = Hybrid()
print(Nexon.tank)
print(Nexon.kWH)


print(Nexon.tank_cap)
print(Nexon.kWH_cap)

print(Nexon.recharge())
print(Nexon.kWH)