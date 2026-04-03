#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head is None:
        return node
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = node
    return head


if __name__ == "__main__":
    llist_count = int(input())
    llist = SinglyLinkedList()
    for _ in range(llist_count):
        llist_item = int(input())
        llist.head = insertNodeAtTail(llist.head, llist_item)

    cur = llist.head
    while cur is not None:
        print(cur.data)
        cur = cur.next
