# coding=utf-8
# 进阶Python

# 面向对象编程
class Person(object):
    pass


p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, key=lambda x: x.name)

print(L2[0].name)
print(L2[1].name)
print(L2[2].name)


# Person类的__init__方法，除了接受 name、gender 和 birth 外，还可接受任意关键字参数，并把他们都作为属性赋值给实例。
class Person(object):
    def __init__(self, myname, sex, birth, **kw):
        self.name = myname
        self.sex = sex
        self.birth = birth
        self._title = 'Mr'
        # self.__dict__.update(kw)将job传到了**kw里，**kw相当于接收了任意关键字参数
        self.__dict__.update(kw)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
print(xiaoming.name)
print(xiaoming.sex)
print(xiaoming.job)
print(xiaoming._title)


# python中访问限制
class Person(object):
    def __init__(self, name, score):
        self.__myname = name
        self.__score = score

    def get_myname(self):
        return self.__myname

    # 创建可以访问内部score的方法
    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


p = Person('Bob', 59)
p.set_score(60)
print('p.get_myname()=', p.get_myname())
print('p.get_score()=', p.get_score())


# 创建类属性
class Person(object):
    count = 0

    def __init__(self, name):
        self.getname = name
        Person.count = Person.count + 1


p1 = Person('Bob')
print(Person.count)

p2 = Person('Alice')
print(Person.count)

p3 = Person('Tim')
print(Person.count)


# 定义实例的方法
class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print(p1.name, p1.get_grade())
print(p2.name, p2.get_grade())
print(p3.name, p3.get_grade())
