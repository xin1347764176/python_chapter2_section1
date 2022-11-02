class phone():
    __is_5g_enable=True
    def __check_5g(self):
        if self.__is_5g_enable:#u should use self
            print("5g on")
        else:
            print("5g off,please use 4g")
    def call_by_5g(self):
        self.__check_5g()  #self
        print("calling")

phone=phone()
phone.call_by_5g()
