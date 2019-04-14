# 导入系统模块、第三方模块、自定义模块,模块在第一次被导入时,生成pyc文件
# import 包名.模块名  # 不推荐
# import py.demo03 as pd  # 推荐
# pd.show()
# print(pd.a)

import random
# from 包名.模块名 import 对象名,对象名 as 别名  此方式推荐
from py.demo03 import a, b, show, Student


# 底下的show会覆盖上面的show
def show():
    print('main.py的show()')


print(a, b)
show()
stu = Student('s1')
stu.show()
