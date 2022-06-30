for i in range(1,21):
    print(i,end = ' ')

def say_hello(time):
    """
        the func is to print hello
        """
    for i in range(time):
        print("hello", end = ' ')

say_hello(5)

import pl
if __name__ == '__main__':
    pl.print_line("!", 20)

num1 = 2
num2 = 2
num3 = num1
print(id(num1))
print(id(num2))
print(id(num3))

bool1 = True
bool2 = True
print(id(bool1))
print(id(bool2))

a = 1.35
print(id(a))
b = 1.35
a = 2.2
print(id(b))
print(id(a))

tp1 = (1,2,3)
tp2 = (1,2,3)
print(id(tp1))
print(id(tp2))

def change_list(demo_list1):
    demo_list1[0] = 2
    demo_list1[1] = 3
    demo_list1[2] = 4
    print(id(demo_list1))

demo_list = [1,2,3]
print(id(demo_list))
change_list(demo_list)

num = 10
def sum1():
    num = 10
    print(num)
    for i in range(100):
        num += i
    print(num)

print(num)

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,3,5,9,12]
same = []
for i in list1:
    for j in list2:
        if i == j:
            same.append(j)
print(same)

list3 = [1,1,3,4,7,1,1,10,12,1,1,1,8]
list3.sort()
most = list3[len(list3)//2]
print(most)