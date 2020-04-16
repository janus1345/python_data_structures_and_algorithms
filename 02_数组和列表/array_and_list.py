# -*- coding: utf-8 -*-
# @Time : 2020/4/16 16:28
# @Author : tanyao1345@163.com
# @FileName: array_and_list.py
# @Software: PyCharm
# @desc:

from array import array

arr = array('u', 'asdf')

print(arr[0], arr[1], arr[2], arr[3], type(arr[1]))

# 实现定长的 Array ADT，省略边界检查


class Array:

    def __init__(self, size):
        self.size = size
        self._items = list()

    def __getitem__(self, index):
        return self._items[index]