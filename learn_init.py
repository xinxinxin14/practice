# _*_coding:utf-8 _*_
class Test(object):
    """
    用于初始化类
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def res(self):
        return (self.a, self.b)

t = Test(321,3213)
print(t.res())


"""
(100, 200)
"""
