# -*- coding: utf-8 -*-


class Node():
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def __str__(self):
        return '<Node: value:{}, next:{}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList():
    """单链表 ADT"""

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()  # 默认 root 节点指向 None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length


    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("Full")
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            # 加到最后一个节点的后面
            tailnode.next = node
        # 最后一个节点变成了当前节点
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("Full")
        node = Node(value)
        if self.tailnode is None:
            # 如果原链表为空，插入第一个元素需要设置 tailnode
            self.tailnode = node

        headnode = self.root.next
        node.next = headnode
        self.root.next = node
        self.length += 1

    def iter_node():
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not Node:
            yield curnode


    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        """将前一个节点的next指向被查询节点的下一个节点"""

        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:
                    if prevnode is self.root:
                        self.tailnode = None
                     else:
                        self.tailnode = prevnode
                del curnode
                self.length -= 1
            else:
                prevnode = curnode
        return -1

    def find(self, value):
        index = 0
        for curnode in self.iter_node():
            if curnode.value == value:
                yield index
            else:
                index += 1
        return -1

    def popleft(self):
        """删除第一个链表节点"""
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            self.root.next = Node
            self.length = 0
            self.tailnode = Node

    def reverse(self):
        """反转链表"""
        curnode = self.root.next
        self.tailnode = curnode   # 反转过后 第一个节点就是 tailnode

        prevnode = None
        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode
            if nextnode is None:
                self.root.next = curnode # 将最后一个节点变成 headnode
            prevnode = curnode
            curnode = nextnode


