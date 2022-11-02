class Phone:
    IMEI=None
    producer="HdM"
    def call_by_4g(self):
        print("5G CALL")

class Phone2022(Phone):
    producer="conde"
    def call_by_4g(self):
        print("new function 5g")
        # #way1
        # print(f"父类的厂商是{Phone.producer}")
        # Phone.call_by_4g(self)
        #way2
        print(f"父类的厂商是{super().producer}")
        super().call_by_4g()
        print("done")

phone=Phone2022()
phone.call_by_4g()
print(phone.producer)