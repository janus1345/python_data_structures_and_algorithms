# -*- coding: utf-8 -*-

class Node():
    def __init__(self, value=None, next=None):
        self.next = next
        self.value = value

    def __str__(self):
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList():
    """ 链表 ADT
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("LinkedList is Full")
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        head = self.root.next
        self.root.next = node
        node.next = head
        self.length += 1
    def iter_node():
        curnode = self.root.next
        while curnode is not self.self.tailnode:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        curnode = self.root.next
        prevnode = self.root
        for curnode in self.iter_node() :
            if curnode.value == value:
                prevnode.next = curnode.next
                del curnode
                self.length -= 1
                return 1
            else:
                prevnode = curnode
        return -1

    def find(self, value):
        index = 0
        for curnode in self.iter_node():
            if curnode.value == value:
                return index
            index += 1
        return -1

    def popleft(self):
        curnode = self.root.next
        if curnode is None:
            raise Exception('pop from empty LinkedList')
        self.root.next = curnode.next
        self.length -= 1
        value = curnode.value
        del curnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0

""" 实现Queue"""


class EmptyError(Exception):
    pass


class Queue():
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_link_list = LinkedList()

    def __len__(self):
        return len(self._item_link_list)
    def push(self, value):
        return self._item_link_list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_link_list.popleft()


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3
    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        q.pop()
    assert 'empty queue' == str(excinfo.value)


""" 使用collections.deque实现队列
"""


from collections import deque
class MyQeque():
    def __init__(self):
        self.items = deque()

    def append(self, val):
        return self.items.append(val)
    def pop(self):
        return self.items.popleft()

    def __len__(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def front(self):
        return self.items[0]
