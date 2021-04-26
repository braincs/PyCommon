#!usr/bin/env python  #-*- coding:utf-8 _*-  """ 
"""
@file: simple_deep_copy.py 
@version:
@time: 2021/04/26 
@author: shuai
@function: 
"""
import copy

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = a
    print(id(a))
    print(id(b))

    a.append(1)
    print(a, b)
    b.append(2)
    print(a, b)
    # 可以发现变量“a”,“b”指向同一块内存区域，所以对其中一个的操作将会影响到另一个。

    print('========================')
    c = [1, 2, 3, 4]
    d = c
    e = copy.copy(c)
    f = copy.deepcopy(c)
    print(c, d, e, f)
    print(id(c), id(d), id(e), id(f))

    e.append(3)
    print(c, d, e, f)
    f.append(4)
    print(c, d, e, f)
    # 采用copy方式会将对象拷贝一份到新的内存地址中,“e”和“f”和 c的id不同
    # copy和deepcopy有和区别

    g = [1, [1, 2, 3], 3]
    h = g
    i = copy.copy(g)
    j = copy.deepcopy(g)
    print(id(g), id(h), id(i), id(j))
    print(id(g[1]), id(h[1]), id(i[1]), id(j[1]))
    g[1].append(1)
    print(g, h, i, j)
    h[1][1] = 1
    print(g, h, i, j)
# 虽然使用copy()方法，变量“i”指向的内存和“g”不再相同，
# 但是“i”和“g”第二层列表还是同一个地址。但是deepcopy()方法第二层列表的地址也和“g”不同了。
# 所以我们说，copy()是浅拷贝，不管对象多么复杂，都只拷贝第一层。