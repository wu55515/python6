# class Node:
#     def __init__(self, elem = 0, lele = None, rele = None):
#         self.elem = elem
#         self.lele = lele
#         self.rele = rele
#
# class Tree:
#     def __init__(self):
#         self.root = None
#         self.queue = []
#
#     def tree_build(self, element):
#         new_node = Node(element)
#         self.queue.append(new_node)
#         if self.root is None:
#             self.root = new_node
#         else:
#             if self.queue[0].lele is None:
#                 self.queue[0].lele = new_node
#             elif self.queue[0].rele is None:
#                 self.queue[0].rele = new_node
#                 self.queue.pop(0)
#     def preorder(self, node):
#         if node:
#             print(node.elem, end = '')
#             self.preorder(node.lele)
#             self.preorder(node.rele)
#
#     def mid(self, node):
#         if node:
#             self.mid(node.lele)
#             print(node.elem, end = '')
#             self.mid(node.rele)
#
#     def last(self, node):
#         if node:
#             self.last(node.lele)
#             self.last(node.rele)
#             print(node.elem, end = '')
#
# tree=Tree()
# for i in 'abcdefghij':
#     tree.tree_build(i)
# tree.preorder(tree.root)
# print()
# tree.mid(tree.root)
# print()
# tree.last(tree.root)
# print()


import random
arr = [random.randint(0, 100) for i in range(100)]
print(arr)
# def bubble_sort(a):
#     for i in range(len(a)-1, 0, -1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# print(bubble_sort(arr))
#
# def select_sort(a):
#
#     for i in range(len(a)-1):
#         min_num = a[i]
#         min_ind = i
#         for j in range(i+1,len(a)):
#             if a[j] < min_num:
#                 min_num = a[j]
#                 min_ind = j
#         a[i], a[min_ind]= a[min_ind], a[i]
#     return a
#
# print(select_sort(arr))

# def insert_sort(a):
#     for i in range(1,len(a)):
#         standard = a[i]
#         index = i
#         for j in range(i-1,-1,-1):
#             if standard < a[j]:
#                 a[j+1] = a[j]
#                 index = j
#         a[index] = standard
#     return a
# print(insert_sort(arr))
#
# def partier(left, right, list1):
#     index = left
#     for i in range(left,right):
#         if list1[i] < list1[right]:
#             list1[index], list1[i] = list1[i], list1[index]
#             index += 1
#     list1[index], list1[right] = list1[right], list1[index]
#     return index
#
#
# def quick(left, right, list1):
#     if left < right:
#         middle = partier(left, right, list1)
#         quick(left, middle-1, list1)
#         quick(middle + 1, right, list1)

# def adjust(fa, num, a):
#     son = 2*fa + 1
#     while son < num:
#         if son + 1 < num and a[son] < a[son + 1]:
#             son += 1
#         if a[son] > a[fa]:  # 拿孩子和父亲比，比父亲大，就交换
#             a[son], a[fa] = a[fa], a[son]
#             fa = son
#             son = 2 * fa + 1
#         else:
#             break
#
# def heap(a, num):
#     for i in range(num//2 - 1, -1, -1):
#         adjust(i, num, a)
#     a[0], a[num-1] = a[num-1], a[0]
#     for i in range(num - 1, 1, -1):
#         adjust(0, i, a)
#         a[0], a[i-1] = a[i-1], a[0]
#
# heap(arr, 10)
# print(arr)

# def merge(left, mid, right, a):
#     help = [0] * 10
#     for i in range(left, right+1):
#         help[i] = a[i]
#     i = left
#     j = mid + 1
#     k = left
#     while i <= mid and j <= right:
#         if help[i] < help[j]:
#             a[k] = help[i]
#             i += 1
#             k += 1
#         if help[j] <= help[i]:
#             a[k] = help[j]
#             j += 1
#             k += 1
#     while i <= mid:
#         a[k] = help[i]
#         i += 1
#         k += 1
#     while j <= mid:
#         a[k] = help[j]
#         j += 1
#         k += 1
#
# def merge_sort(left, right, a):
#     if left < right:
#         mid = (left + right) // 2
#         merge_sort(left, mid, a)
#         merge_sort(mid + 1, right, a)
#         merge(left, mid, right, a)
#
# merge_sort(0, 9, arr)
# print(arr)

def count(a, num_ran):
    list1 = [0] * (num_ran + 1)
    for i in a:
        list1[i] += 1
    k = 0
    for i in range(0,num_ran+1):
        for j in range(list1[i]):
            a[k] = i
            k += 1

count(arr, 100)
print(arr)