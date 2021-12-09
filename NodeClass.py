from imports import *

class LinkedList:

    """
    This class would create a Linked list
    """

    head = None
    tail = None

    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head


    def __str__(self):
        temp = self.head
        output = ""
        while temp:
            for i in temp.val:
                output += str(i) + " "

            output += "\n"
            temp = temp.next

        return output

    def __repl__(self):
        return self.__str__()



    def add(self, val):
        # to add a element in the link list use this function
        temp = Node(val)
        temp.pre = self.tail
        self.tail.next = temp
        self.tail = temp


class Node:
    """
    This is a Node Class
    """
    next = None
    val = None
    pre = None

    def __init__(self, value):
        self.val = value
