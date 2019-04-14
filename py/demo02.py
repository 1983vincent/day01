# 默认继承object
class Animal():

    # 父类有age属性
    def __init__(self, name):
        # 如果_代表保护的属性(子类是可以用的)
        # 如果__代表私有的属性(子类是不可以访问)
        # 如果__属性__特殊属性
        # 如果__方法()__ 特殊方法
        # self.__name = name
        self._name = name

    def show(self):
        print(self._name)


# 编写一个子类,此类继承父类的属性
class Dog(Animal):

    def __init__(self, name, age):
        # 调用父类__init__方法
        super(Dog, self).__init__(name)
        self.age = age

    # 默认可以继承父类的方法,但如果不合适子类可以重写
    def show(self):
        print(self._name, self.age)



dog2 = Animal('旺财X')
dog2.show()

dog = Dog('旺财', 2)
print(type(dog))
# 默认调用的是父类的方法,如果重写肯定调用子类自己的方法
dog.show()



