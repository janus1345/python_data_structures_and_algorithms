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
        self._size = size
        self._items = list()

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    assert len(a) == 10
