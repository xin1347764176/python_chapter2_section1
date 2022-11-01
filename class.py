class Student:
    name=None
    gender=None
    nationality=None
    native_place=None
    age=None
    def say_hi(self):
        print(f"大家好，我是{self.name}")
    def say_hi2(self,msg):
        print(f"大家好，我是{self.name},{msg}")

stu_1=Student()
stu_1.name="allen"
stu_1.gend ="man"
stu_1.nationality="四川"
stu_1.native_place="guandong"
stu_1.age=24
print((stu_1.age))
print((stu_1.name))
print((stu_1.gender))
print((stu_1.nationality))
print((stu_1.native_place))

stu=Student()
stu.name="周杰伦"
stu.say_hi2("woc")
stu_1.say_hi()