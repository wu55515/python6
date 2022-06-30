# class Foo:
#     def func(self):
#         print('i am func')
#     @property
#     def prop(self):
#         print('i am prop')
# f = Foo()
# f.func()
# f.prop
#
# class Goods:
#
#     @property
#     def size(self):
#         return 100
#
# desk = Goods()
# width = desk.size
# print(width)
#
# class Goods:
#     @property
#     def price(self):
#         print('abc')
#
#     @price.setter
#     def price(self, value):
#         print('efg')
#
#     @price.deleter
#     def price(self):
#         print('hahaha')
#
# obj = Goods()
# obj.price
# obj.price = 123
# del obj.price
#
# class Foo:
#     def haha(self):
#         print('haha')
#     Bar = property(haha)
#
# a = Foo()
# a.Bar
# class Province:
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#
#     def func(self, *args):
#         print('haha')
#
# print(Province.__dict__)
# obj = Province('taiwan', 3000)
# print(obj.__dict__)

# def m2():
#     f = open('file', 'r')
#     try:
#         f.write('人生苦短')
#     except IOError:
#         print('ooo')
#     finally:
#         f.close()
#
# def m3():
#     with open('file', 'w', encoding='utf8') as f:
#         f.write('人生苦短')
#
# if __name__ == '__main__':
#     m2()
#     m3()

class File:
    def __init__(self, file_name, open_mode):
        self.file_name = file_name
        self.open_mode = open_mode

    def __enter__(self):
        self.f = open(self.file_name, self.open_mode, encoding='utf8')
        print('it is open.')
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('i will exit.')
        self.f.close()

with File('file', 'w') as f:
    f.write('jianchilianxi')



