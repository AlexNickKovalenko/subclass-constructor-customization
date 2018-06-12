class Person:
    def __init__(self,name,age,job=None,pay=0):
        self.name=name
        self.age=age
        self.job=job
        self.pay=pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self,percent):
        self.pay = int((1+percent)*self.pay)

    def __str__(self):
        return '{0},{1},{2},{3}'.format (self.name,self.age,self.job,self.pay)


class Manager(Person):
    def __init__ (self,name,pay):
        Person.__init__(self,name, 'Mgr',pay)
    def giveRaise(self,percent,bonus):
        self.pay=int((1+percent+bonus)*self.pay)

if __name__=='__main__':
    rec1=Person('Bob Smith',30,job='dev',pay=30000)
    rec2=Person('Edgar Poe',40,job='dev',pay=100000)
    rec3=Person('Adam Spencer',45,job='dev',pay=50000)
    rec3=Manager('Adam Spencer',50000)
    print(rec1.name,rec1.age)
    print(rec2.name,rec2.age)
    print(rec1)
    print('{0} {1}' . format(rec1.name,rec2.age))
    print('pay=',rec1.pay)
    print('rec2=name',rec2.name)
    print('rec2 last name=', rec2.name.split()[-1])
    print('rec2 lastName=', rec2.lastName())
    print('rec1 last name',rec1.lastName())
    print('rec2 pay=', rec2.pay)
    rec2.giveRaise(0.1)
    print('rec2  new pay =',rec2.pay)
    print(rec1)
    print(rec2)
    print(rec3)
    rec3.giveRaise(0.1,0.3)
    print(rec3)
    rec2.giveRaise(0.1)
    print(rec2)
