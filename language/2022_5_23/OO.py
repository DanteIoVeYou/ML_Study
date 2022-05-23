class Person():
    name = 'zhangsan'
    age = 19
    money = 10000000
    def __init__(self, name = 'zhangsan', age = 99, money = 1):
        self.name = name
        self.age = age
        self.money = money
    def GetMoney(self):
        return self.money
    def GetInfo(self):
        print('%s-%s\n'%(self.name, self.age))


p1 = Person('lisi', 20, 999999)
p2 = Person()
p1.GetInfo()
p2.GetInfo()