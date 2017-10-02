class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_node(self,data):
        new_node = Node(data)
        temp = self.head

        if temp is None:
            self.head = new_node
            return

        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def PrintLL(self):
        temp = self.head
        print "Linked List -> ",
        while(temp):
            print temp.data,
            temp = temp.next

    def MiddleNode(self):
        self.slow = self.head
        self.fast = self.head
        if self.head is not None:
            while self.fast is not None and self.fast.next is not None:
                self.slow = self.slow.next
                self.fast = self.fast.next.next

            print "\nThe middle element is %s\n" %(self.slow.data)

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_node(1)
    LL.PrintLL()
    LL.MiddleNode()
    LL.add_node(2)
    LL.PrintLL()
    LL.MiddleNode()
    LL.add_node(3)
    LL.PrintLL()
    LL.MiddleNode()
    LL.add_node(4)
    LL.PrintLL()
    LL.MiddleNode()
    LL.add_node(5)
    LL.PrintLL()
    LL.MiddleNode()
