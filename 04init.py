# 构造方法名称__init__
class Student:
    name=None
    age=None
    tel=None
    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print("student类创建了一个对象")
stu=Student("周杰伦",32,"12354")
print(stu.name)
print(stu.age)
print(stu.tel)

