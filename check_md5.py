# -*- coding:utf-8 -*-
"""
@version:
author: Shuai
@time: 2020/03/11
@file: checkMD5.py
@function:
"""
import os
import hashlib
import argparse

src_folder = '/Users/changshuai/images/'
dst_folder = '/Users/changshuai/backup-images/images/'

ir_src_folder = src_folder + 'IR/'
dep_src_folder = src_folder + 'Dep/'
rgb_src_folder = src_folder + 'RGB/'
jpg_src_folder = src_folder + 'JPG/'

ir_dst_folder = dst_folder + 'IR/'
dep_dst_folder = dst_folder + 'Dep/'
rgb_dst_folder = dst_folder + 'RGB/'
jpg_dst_folder = dst_folder + 'JPG/'

ir_md5_list = []
dep_md5_list = []
rgb_md5_list = []
jpg_md5_list = []


def file_as_bytes(file):
    with file:
        return file.read()


def get_md5_list(folder):
    md5_list = []
    files = os.listdir(folder)
    for i in range(len(files)):
        file = os.path.join(folder, files[i])
        # print(i, file, hashlib.md5(file_as_bytes(open(file, 'rb'))).hexdigest())
        md5_list.append(hashlib.md5(file_as_bytes(open(file, 'rb'))).hexdigest())
    return md5_list


def get_filename_md5_list(folder):
    md5_list = []
    files = os.listdir(folder)
    for i in range(len(files)):
        file = os.path.join(folder, files[i])
        # print(i, file, hashlib.md5(file_as_bytes(open(file, 'rb'))).hexdigest())
        md5_list.append((i, file, hashlib.md5(file_as_bytes(open(file, 'rb'))).hexdigest()))
    return md5_list


def compare_files_md5(src_folder, dst_folder):
    src_md5s = get_filename_md5_list(src_folder)
    dst_md5s = get_md5_list(dst_folder)
    fail_list = []
    succ = 0
    fail = 0
    for _, name, srcmd5 in src_md5s:
        if srcmd5 not in dst_md5s:
            # print(name, "not found")
            fail_list.append(name)
            fail += 1
        else:
            succ += 1
    # print(len(src_md5s), "checked: ", ir_src_folder, fail, "not passed")
    return succ, len(src_md5s), fail_list


def check_rgb_ir_dep_md5():
    ir_md5_list = get_md5_list(ir_dst_folder)
    print(len(ir_md5_list), ir_md5_list)
    dep_md5_list = get_md5_list(dep_dst_folder)

    rgb_md5_list = get_md5_list(rgb_dst_folder)

    jpg_md5_list = get_md5_list(jpg_dst_folder)

    ir_src_md5_list = get_filename_md5_list(ir_src_folder)
    dep_src_md5_list = get_filename_md5_list(dep_src_folder)
    rgb_src_md5_list = get_filename_md5_list(rgb_src_folder)
    jpg_src_md5_list = get_filename_md5_list(jpg_src_folder)

    count = 0
    for _, name, srcmd5 in ir_src_md5_list:
        if srcmd5 not in ir_md5_list:
            print(name, "not found")
    print(len(ir_src_md5_list), "checked: ", ir_src_folder, count, "not passed")

    count = 0
    for _, name, srcmd5 in dep_src_md5_list:
        if srcmd5 not in dep_md5_list:
            print(name, "not found")
    print(len(dep_src_md5_list), "checked: ", dep_src_folder, count, "not passed")

    count = 0
    for _, name, srcmd5 in rgb_src_md5_list:
        if srcmd5 not in rgb_md5_list:
            print(name, "not found")
    print(len(rgb_src_md5_list), "checked: ", rgb_src_folder, count, "not passed")

    count = 0
    for _, name, srcmd5 in jpg_src_md5_list:
        if srcmd5 not in jpg_md5_list:
            print(name, "not found")
            count += 1
    print(len(jpg_src_md5_list), "checked: ", jpg_src_folder, count, "not passed")


def main():
    parser = argparse.ArgumentParser(
        description='convert raw image saved by core into image format',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('input', help='inputs: src, dst folder', nargs=2)
    args = parser.parse_args()
    print(args.input)

    sfolder = args.input[0]
    dfolder = args.input[1]
    same_count, size, namelist = compare_files_md5(sfolder, dfolder)
    print("compare: {}, same: {}".format(same_count, size))
    if namelist:
        print("Details: ", namelist)


if __name__ == '__main__':
    # get target md5 list
    # compare_files_md5("/Users/changshuai/images/JPG/", "/Users/changshuai/待分类图片数据/")
    main()
