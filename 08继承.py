class Phone:
    IMEI=None
    producer="HdM"
    def call_by_4g(self):
        print("ITCAST")

class Phone2022(Phone):
    face_id="000"
    def call_by_5g(self):
        print("new function 5g")

phone=Phone2022()
print(phone.IMEI)
print(phone.producer)
phone.call_by_5g()
phone.call_by_4g()

class NFCReader:
    nfc_type="第五代"
    producer="HM"
    def read_card(self):
        print("NRC读卡")
    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type="红外遥控"
    def control(self):
        print("红外遥控开了")

class MyPhone(Phone,NFCReader,RemoteControl):
    pass

myphone=MyPhone()
myphone.call_by_4g()
myphone.write_card()
print(myphone.producer)