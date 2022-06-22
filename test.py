import os
import subprocess as sub
# import time
#
# import PyInstaller as ps
# print(ps.__file__)
# time.sleep(5)
# # result = sub.Popen("D:\soft\\notepad++\\notepad++.exe", shell=True, stdout=sub.PIPE, stderr=sub.PIPE)
# result.wait()
# if result.returncode == 0:
# 	print("执行完毕")
# else:
# 	print("执行错误")
# ls = [2, 4, 5, 6, 7]
# for var in ls:
#     if var % 2 == 0:
#         ls.remove(var)
# print(ls)
# print(3<4<5)
# import io
# s = "hello,sxt"
# sio = io.StringIO(s)
# print(sio.seek(5))
# sio.write("g")
# print(sio.getvalue())
# a = [1, 3, 4, 2, 5, 7, 6]
# print(id(a))
# b = a.sort()
# print(id(b))
# # print(id(a))
# # print(a)
# a = sorted(a, reverse=True)
# print(a)
# print(id(a))


# a = "abc"
# print(a.title())
# print(a.ljust(10, "*"))
# print("abc{0:+<10}".format("er"))
# print("我是{0:-^10},今年{1:=>4}".format("小明", 15))
# print("我是{0}, 我的存款有{1:.2f}".format("小李", 3.1245))


# s = (x*2 for x in range(5))
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# print(s.__next__())
# d = dict()
# d.
# class Listinfo:
#     def __init__(self, data):
#         self.data = data
#         self.size = len(data)
#
#     def add_key(self, key):
#         l1 = []
#         if type(key) == str or type(key) == int:
#             l1.append(key)
#             self.data = self.data + l1
#             self.size = self.size + 1
#             return self.data, self.size-1
#         else:
#             print("add_key fail, type not str or int")
#     def get_key(self, num):
#
#
#
# l = Listinfo([2])
# print(l.add_key(1))
# print(l.add_key("sss"))
# print(l.size
# s = 'aaabbccccd'
# count = 1
# f = s[0]
# result = ""
# for i in range(1, len(s)):
#     if s[i] == f:
#         count += 1
#     else:
#         result = result + f + str(count)
#         f = s[i]
#         count = 1
# result = result + f + str(count)
# print(result)
class listinfo:
    def __init__(self,data_list):
        self.data_list = data_list
        self.size = len(data_list)

    def add_key(self, key):
        self.data_list = self.data_list + list(key)
        self.size += len(list(key))
        print(self.data_list)

    def get_key(self, key_num):
        key = self.data_list[key_num]
        print(key)

    def update_list(self, target_list):
        self.data_list = self.data_list + target_list
        print(self.data_list)

    def del_key(self):
        del self.data_list[-1]
        print(self.data_list)


listinfo1 = listinfo(["a"])
listinfo1.add_key("c")
# listinfo1.get_key(0)
listinfo1.del_key()