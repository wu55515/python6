# import re
# name_list = ['http://www.interoem.com/messageinfo.asp?id=35',
# 'http://3995503.com/class/class09/news_show.asp?id=14',
# 'http://lib.wzmc.edu.cn/news/onews.asp?id=769',
# 'http://www.zy-ls.com/alfx.asp?newsid=377&id=6',
# 'http://www.fincm.com/newslist.asp?id=415']
# for name in name_list:
#     ret = re.findall(r"//.*(?:com|cn)/",name)
#     for i in ret:
#         res = re.sub(r'/+', '', i)
#         print(res)
# for name in name_list:
#     ret=re.match('www\.[\w]+\.(com|edu|net)$',name)
#     if ret:
#         print('{} 符合要求'.format(ret.group()))
#     else:
#         print('{} 不符合要求'.format(name))
# import re
# with open("test.txt", encoding='utf-8') as test:
#     for line in test:
#         if re.findall(r"<[^>]*>|&nbsp;|\n",line.strip()):
#             res = re.sub(r"<[^>]*>|&nbsp;|\n", "", line.strip())
#             print(res)


class Parents:
    def __init__(self, name, *args, **kwargs):
        print('Parents is start.')
        self.name = name
        print('The P is stop.')

class Son1(Parents):
    def __init__(self, name, age, *args, **kwargs):
        print('son1 init is start.')
        self.age = age
        super().__init__(name, *args, **kwargs)
        print('son1 is stop.')

class Son2(Parents):
    def __init__(self, name, gender, *args, **kwargs):
        print('son2 init is start.')
        self.gender = gender
        super().__init__(name, *args, **kwargs)
        print('son2 is stop.')

class GrandSon(Son1,Son2):
    def __init__(self, name, age, gender):
        print('Grandson is start.')
        super().__init__(name, age, gender)
        print('Grandson is stop.')
print(GrandSon.__mro__)
res = GrandSon('sunzi', 10, 'boy')
print('name',res.name)
print('age', res.age)
print('gender', res.gender)