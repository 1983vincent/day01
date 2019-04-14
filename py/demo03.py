# py结尾的文件都是模块
# 模块采用的是下划线命名法
# 一个模块可以有 变量、函数、类

a = 10
b = 20


# 定义了一个函数
def show():
    print('show()..............')


# 定义一个类
class Student(object):

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f'学生姓名为{self.name}')


print(__name__)

# 测试模块的代码,__name__特殊属性
if __name__ == '__main__':
    show()
    stu = Student('张三')
    stu.show()
