# -*- coding:utf-8 -*-
#key属性的使用

a = [222,333,444,1111]

print max(a)

print max(a, key = str)

print max(a, key = lambda item:len(str(item)))

b = ((3, 5, 5),(4, 5, 6),(4, 4, 7))

print max(b)

print max(b, key = lambda item : (item[0],item[2]))

def sort1(item):
    return (item[1])

print max(b, key = sort1)

#max函数的hack。

#问题描述：取字典里value最大的；如果value相同，则取key最大。
prices = {
    u'A': 444,
    u'B': 555,
    u'C': 666,
    u'D': 333
}

# #max函数对dict会取其key进行排序。
# print max(prices)

# dict的反转。
prices_items = prices.items()
# 1.zip  压缩。
prices_re = dict(zip(prices.values(),prices.keys()))
print max(zip(prices.values(),prices.keys()))
print max(prices_re)
# 2.列表推导式。
prices_re = {value:key for (key, value) in prices_items}
print max(prices_re)


# #扩展：反转list的三种方式
# tel_list = ['110', '120', '114', '12580']
# # 1.reversed()    返回的是一个迭代器。
# print type(reversed(tel_list))
# print list(reversed(tel_list))
# # 2.sorted        reverse参数表示顺序，false表示升序，true表示降序。
# print sorted(tel_list,cmp=None,key=None,reverse=False)
# # 3.分片          第一个冒号：开始位置；第二个冒号：结束位置（不包含）；第三个冒号，步长，为负则表示从end->start。
# print tel_list[::-1]
