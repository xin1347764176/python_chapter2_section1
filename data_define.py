class Record:
    def __init__(self,date,order_id,money,province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province
    def __str__(self):    #魔术方法，不然输出是地址
        return f"{self.date},{self.order_id},{self.money},{self.province}"