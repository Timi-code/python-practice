#!/usr/bin/env python3   让文件可以直接在Unix/Linux/Mac上运行
# -*- coding: utf-8 -*-  文件编码

"a test module"  # 第一个字符串作为注释

__author__ = "timi"  # 文件的作者

import sys  # 导入模块


def test():
    args = sys.argv  # argv 运行该文件的所有参数，至少有一个 文件名本身  list
    if len(args) == 1:
        print("Hello, world!")
    elif len(args) == 2:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")


if __name__ == "__main__":  # 如果是命令行执行该文件 那么他们就会相等
    test()
