# 私有成员方法和变量,class内部自己使用
class Phone:
    IMEI=None
    producer=None
    __current_voltage=0.5
    def call_by_5g(self):
        print("5g calling")
    def __keep_single_core(self):
        print("cpu work ")

    def call_by_5g(self):
        if self.__current_voltage>=1:  #u should use "self"
            print("5g prepared")
        else:
            self.__keep_single_core()
            print("power off")

phone=Phone()
# phone.__current_voltage()
# phone.__keep_single_core() #you can not use it
phone.call_by_5g()