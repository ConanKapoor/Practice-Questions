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

    def PrintLL(self,number):
        temp = self.head
        print "Linked list %s -> " %number
        while(temp):
            print temp.data,
            temp = temp.next
        print "\n"

    def SortedMerge():


if __name__ == '__main__':
    LL1 = LinkedList()
    LL2 = LinkedList()
    LL1.add_node(5)
    LL2.add_node(2)
    LL1.PrintLL(1)
    LL2.PrintLL(2)
    LL1.add_node(10)
    LL2.add_node(3)
    LL1.PrintLL(1)
    LL2.PrintLL(2)
    LL1.add_node(15)
    LL2.add_node(20)
    LL1.PrintLL(1)
    LL2.PrintLL(2)

    SortedMerge(LL1,LL2)
