class Student:
    # 属性
    name = None
    age = None
    address = None

    # 构造方法
    def __init__(self):
        self.name = input("请输入学生姓名：")
        self.age = int(input("请输入学生年龄："))
        self.address = input("请输入学生地址：")

for item in range(1, 11):
    print(f"当前录入第{item}位学习信息，总共需录入10位学习信息")
    stu = Student()
    print(f"学生{item}信息录入完成，信息为：【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.address}】")