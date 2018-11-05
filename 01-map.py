
"""
map():python的内置函数，直接使用类似print()
会根据提供函数对指定的序列做映射


描述：
    创建一个迭代器，使用每一个迭代器，当最短的迭代被耗尽时终止
格式：
map(function,iterables)
function:函数，有两个参数

iterables：一个或者多个序列

   python2:返回的是一个列表
   python3：迭代器

"""
# a = (1,2,3,4,5)
# b = [1,2,3,4,5]
# c = "laowang"
#
# la = map(str,a)
# # print(list(la))
# lb = map(str,b)
# # print(list(lb))
# lc = map(str,c)
# print(list(lc))

#将单个字符转换成对应的字面量整数
# def chr2int(chr):
#     return {"0":0,"1":1,"2":2,"3":3,"4":4}[chr]
# d = ["1","2","3"]
# ld = map(chr2int,d)
# print(list(ld))
numbers = ['1','2','3','4','5']
print(list(map(int, numbers)))




