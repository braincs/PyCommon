# -*- coding:utf-8 -*-
"""
@version:
author: Shuai
@time: 2020/08/05
@file: echo_path_to_file.py
@function: echo file path in the current folder to target file
"""

import os
import argparse


def walk_folder_generate_file(level=3, folder='.', label_file='labels.csv'):
    """
    recurse folder and output absolute path to label_file
    :param level: effective folder depth level
    :param folder: input folder
    :param label_file: label_file
    :return: none
    """
    if not os.path.exists(folder):
        return
    file = os.path.join(folder, label_file)
    with open(file, 'w') as f:

        for root, dirs, files in os.walk(folder):
            for name in files:
                path = os.path.join(root, name)
                segs = path.split(os.sep)
                if len(segs) > level:
                    continue
                if name.startswith('.'):
                    continue

                print(path)
                f.write(path+'\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='generate file path under current folder',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('-l', '--level', required=False, help='recursive level', nargs=1, default=3)
    parser.add_argument('-i', '--input', required=False, help='input folder', nargs=1, default='.')
    parser.add_argument('-o', '--output', required=False, help='output file', nargs=1, default='labels.csv')
    args = parser.parse_args()
    print(args.input, args.level, args.output)
    walk_folder_generate_file(args.level, args.input, args.output)

    # for name in dirs:
    #     print(os.path.join(root, name))
    # for root, dir, files in os.walk("."):
    #     print(root)
    #     print(dir)
    #     # print(files)
    #     for file in files:
    #         print(type(root))
    #         print(type(dir))
    #         print(type(file))
    #         print(file)
    # print(os.path.join(root, dir, file))
    # path = root.split(os.sep)
    # print(path)
    # print(dir)
    # # print((len(path) - 1) * '---', os.path.basename(root))
    # for file in files:
    #     print(len(path) * '---', file)
