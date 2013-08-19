# Copyright Qwilt, 2013
# 
# The code contained in this file may not be used by any other entities without explicit written permission from Qwilt.
# 
# Author: adana

class Node(object):
    def __init__(self):
        self.prev = None
        self.next = None

    def insertToList(self, prev, next):
        self.prev = prev
        if prev:
            prev.next = self

        self.next = next
        if next:
            next.prev = self

    def removeFromList(self):
        if self.prev != None:
            self.prev.next = self.next

        if self.next != None:
            self.next.prev = self.prev

        self.prev = None
        self.next = None

    def isInList(self):
        if (self.next == None) and (self.prev == None):
            return False

        return True

class LinkedList(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.insertToList(None, self.tail)
        self.__numItems = 0

    @property
    def numItems(self):
        return self.__numItems

    def insert(self, next, item):
        item.insertToList(next.prev, next)
        self.__numItems += 1

    def pushHead(self, item):
        self.insert(self.head.next, item)
        
    def pushTail(self, item):
        self.insert(self.tail, item)

    def popHead(self):
        if self.head.next == self.tail:
            return None

        item = self.head.next
        item.removeFromList()
        self.__numItems -= 1

        return item

    def popTail(self):
        if self.tail.prev == self.head:
            return None

        item = self.tail.prev
        item.removeFromList()
        self.__numItems -= 1

        return item

    def remove(self, item):
        item.removeFromList()
        self.__numItems -= 1

    def __iter__(self):
        curr = self.head.next

        while curr != self.tail:
            yield curr
            curr = curr.next

    def __repr__(self):
        return "LinkedList([%s])" % ', '.join(map(repr,self))


class IntListItem(Node):
    def __init__(self, val):
        Node.__init__(self)
        self.val = val

    def __repr__(self):
        return "%d" % self.val



