
# 1: python中所有py结尾的文件都称为模块
# 2: 一个模块可以包含多个类,函数,变量,而且模块名称是小写

# 自定义类型默认继承object
class Person(object):

    # 特殊方法__方法名__(): 在创建对象时会自动调用
    # __init__在对象初始化时会自动调用
    # self代表this,此参数系统传入
    def __init__(self, name, age):
        print('1', self)
        # 当前对象有name age属性
        self.name = name
        self.age = age

    # self永远指向当前对象
    def show(self):
        print('3',self)
        print(f'姓名为:{self.name},年龄为:{self.age}')

    # __del__在垃圾回收时自动被调用
    def __del__(self):
        print('4',self)


# 先有类才有对象,在类中可以定义属性和方法,然后对象可以使用
p = Person('小强',18)
# 打印对象的ID和类型
p.show()
# 回收此对象,默认会调用__del__方法

p2 = Person('旺财',28)
p2.show()
