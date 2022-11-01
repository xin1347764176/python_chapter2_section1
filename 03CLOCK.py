class Clock:
    id=None
    price=None
    def ring(self):
        import winsound
        winsound.Beep(2000,1000)
clock1=Clock()
clock1.id="asdf"
clock1.price=19.3
print(f"闹钟id{clock1.id},price{clock1.price}")
clock1.ring()