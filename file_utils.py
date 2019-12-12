# -*- coding:utf-8 -*-

"""
@version:
author:changshuai
@time: 2019/12/12
@file: file_utils.py
@function: related file utils
"""
import os


class FileUtil:

    @classmethod
    def list_all_file(cls, directory="./"):
        """
        print all file under directory
        :param directory: directory want to see,
                default: current directory
        :return: none
        """
        # compatible with abs path
        pwd = os.path.join(os.getcwd(), directory)
        files = os.listdir(pwd)
        for f in files:
            print(f)


if __name__ == '__main__':
    FileUtil.list_all_file("./test")
