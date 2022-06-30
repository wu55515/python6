import time
# def nonl():
#     x = 20
#     def small():
#         nonlocal x
#         print('The first x is %d' %x)
#         x = 10
#         print('The second x is %d' %x)
#     return small
#
# res = nonl()
# res()

# def outer(func):
#     print('start')
#     def call_func():
#         print('11111')
#         func()
#     return call_func
#
# @outer
# def user():
#     print('hahaha')
#
# user()

# def one(func):
#     print('i am one one.')
#     def call_back():
#         print('i am one two.')
#         func()
#     return call_back
#
# def two(func):
#     print('i am two one.')
#     def call_back():
#         print('i am two two.')
#         func()
#     return call_back
#
#
# @one
# @two
# def three():
#     print('i am the content.')
#
# three()

# def acc(func):
#     def call_func():
#         start = time.time()
#         func()
#         stop = time.time()
#         total = stop-start
#         print('the total time of the program is %d' %total)
#     return call_func
#
# @acc
# def funn():
#     print('start')
#     for i in range(1000000000):
#         pass
#
# funn()

# from time import ctime, sleep
# def timefun_arg(pre='hello'):
#     def timefun(func):
#         def wrapped_func():
#             print('%s called at %s %s' %(func.__name__, ctime(), pre))
#             return func()
#         return wrapped_func
#     return timefun
# @timefun_arg('java')
# def foo():
#     print('i am java.')
#
# @timefun_arg('python')
# def too():
#     return 'python'
#
# foo()
# sleep(1)
# foo()
#
# print(too())
# sleep(2)
# print(too())

# class Test(object):
#     def __init__(self, func):
#         print('initization.')
#         print('func_name is %s' %func.__name__)
#         self.func = func
#     def __call__(self, *args, **kwargs):
#         print('hahaha')
#         self.func()
#
# @Test
# def foo():
#     print('class decorate.')
#
# foo()

from functools import wraps
def my_dec(func):
    @wraps(func)
    def www(*args, **kwargs):
        '''decorator'''
        print('lalalalala')
        return func(*args, **kwargs)
    return www

@my_dec
def foo():
    '''describition'''
    print('hahahaha')

print(foo.__name__, foo.__doc__)














