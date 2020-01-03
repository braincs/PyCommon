# -*- coding:utf-8 -*-
"""
@version:
author: Shuai
@time: 2020/01/03
@file: argparse.py
@function:
"""
import argparse

# 基本用法：positional arguments 定位参数，不用加 '-'
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number",
                    type=int)

# 基本用法：optional arguments 定位参数，通过 '-' 指定或 '--' 指定
# -v必须指定参数值，否则就会报错
parser.add_argument("-v", "--verbose", help="increase output verbosity")

# action='store_true'
# -v不用指定参数值，有 '-v' 为True，没有为 False
parser.add_argument("-v", "--verbose", help="increase output verbosity", action='store_true')

parser.add_argument("-n", "--name", help="current name")
# 可选值 choices=[]
# 配置默认值 default=1
# 配置类型 type=类型
parser.add_argument("-i", "--index", type=int, default=1, choices=[0, 1, 2], help="current index")

# 互斥参数
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", help="increase output verbosity", action='store_true')
group.add_argument("-q", "--quiet", help="no output", action="store_true")

args = parser.parse_args()
print(args.echo)
print(args.square ** 2)
if args.verbose:
    print("verbosity turned on:", args.verbose)
if args.index:
    print("index:", args.index)

if args.name:
    print("name:", args.name)
