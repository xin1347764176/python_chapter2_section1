class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):#抽象的父类设计（设计标准） 具体的子类实现（实现标准）
    animal.speak()
dog=Dog()
cat=Cat()
make_noise(Dog())
make_noise(cat)

class AC:
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_l_r(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷技术")
    def hot_wind(self):
        print("美的空调dainreshi加热")
    def swing_l_r(self):
        print("美的左右摆风技术")
class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调核心制冷技术")
    def hot_wind(self):
        print("格力空调dainreshi加热")
    def swing_l_r(self):
        print("格力左右摆风技术")

def make_cool(ac:AC):
    ac.cool_wind()
midea_ac=Midea_AC()
gree_ac=GREE_AC()
make_cool(midea_ac)
make_cool(gree_ac)