# gen = map(int, input().split())
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# dif = 5
# new_dif = 8
# dif = new_dif if new_dif < dif else dif
# print(dif)
#
# lst = [1, 3, 5, 7, 9]
# print(min(lst), max(lst))

# l1 = [22, 33, 1, 2, 7, 4]
# # l2 = sorted(l1)
# # print(l1, l2)
#
# l1.sort()
# print(l1)  # [1, 2, 4, 7, 22, 33] 返回值为None 把原来的列表元素从小到大排序，改变原列表内容
# l2 = [('太白',18), ('alex', 73), ('wusir', 35), ('口天吴', 41)]
# l2.sort(key=lambda x: x[1])
# # print(l2)  # [('太白', 18), ('wusir', 35), ('口天吴', 41), ('alex', 73)]
# l2.sort(key=lambda x: x[1], reverse=True)
# print(l2)  # [('alex', 73), ('口天吴', 41), ('wusir', 35), ('太白', 18)]
#
# def gcd(a, b):
#
#     while b != 0:
#         c = a % b
#         a = b
#         b = c
#
#     return a
#
#
# molecule = 0
#
# for i in range(20):
#     molecule += 2 ** i
#
# gc = gcd(molecule, 2 ** 19)
#
# print(molecule // gc,'/',2 ** 19 // gc, sep='')
# a, b = divmod(10, 3)
# # print(a, b)
# s = ' a sa  da ss daas'
# print(s)
# print(s.strip())
# # strip:空白：空格，\t,\n
# s = '     \n太白\t'
# # print(s)
# print(s.strip())
# from fnmatch import fnmatchcase as match
#
# print(match('88折', '*折'))

# for i in range(2, 3):
#     print(i)

# a = [1, 2, 4]
# a.insert(0,0)
# print(a)
# num_list = [[0] * 5 for i in range(2)]
#
# print(num_list)
# num_list[0][0] = 1
# print(num_list)
# data_map = [[0] * 10 for _ in range(10)]
# data_map = [[0] * 10] * 10  # 不要用这种方式定义，这样data_map[1][1] = 1 会导致每一行的第一个位置都为1
# data_map=[]
# for i in range(10):
#     data_map.append([0 for i in range(10)])
# data_map[1][0] = 1
# print(data_map)

# def func(*args):
#     print(args)
#     if not args:
#         return True
#
# print(func(*[]))

# flag = [True, True, True]
#
# print(all(flag))

a = [0, 1, 3, 5]
for i in range(3, -1, -1):
    print(a[i])

