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
        print "Linked list -> "
        while(temp):
            print temp.data,
            temp = temp.next
        print "\n"

    def Node_From_End(self,position):
        temp = self.head
        count = 0

        while(temp):
            count +=1
            temp = temp.next

        temp = self.head
        for x in range(count-position-1):
            temp = temp.next
        print "Element from %s position from end is: %s" %(position,temp.data)

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_node(1)
    LL.PrintLL()
    LL.add_node(2)
    LL.PrintLL()
    LL.add_node(3)
    LL.PrintLL()
    LL.add_node(4)
    LL.PrintLL()
    LL.add_node(5)
    LL.PrintLL()
    LL.Node_From_End(4)
