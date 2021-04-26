#!usr/bin/env python  #-*- coding:utf-8 _*-  """ 
"""
@file: simple_param_passing.py
@version:
@time: 2020/09/29 
@author: shuai
@function: 
"""
print("hello world!")


def append_a(str):
    str.append('a')


def add_a(a):
    print(id(a))
    a = a + 1
    # a += 1
    print(id(a))
    return a


def display(a):
    print(a)


if __name__ == '__main__':
    a = 2
    print(id(a))
    add_a(a)

    print(id(a))
    display(a)

    str = [1, 2, 3]
    str_2 = str
    append_a(str)
    print(str)
    print(str_2)
    print(id(str))
    print(id(str_2))
    # print(method(3))
