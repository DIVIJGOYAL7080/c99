class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color,
        self.model=model,
        self.company=company,
        self.speed_limit=speed_limit
    def start(self):
        print("started")
    def stop(self):
        print("stopped")
    def accelerate(self):
        print("accelerating")
    def change_gear(self,gear_type):
        self.gear_type=gear_type
        print("gear has been changed")
car=Car("f16","white","a",150)
print(car.start())
print(car.stop())
print(car.accelerate())
print(car.change_gear(40))