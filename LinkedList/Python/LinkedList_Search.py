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

    def printLL(self):
        temp = self.head
        print 'Created linked list is:',
        while(temp):
            print temp.data,
            temp = temp.next
        print '\n'

    def search(self,item):
        temp = self.head

        while temp is not None:
            if temp.data == item:
                print "Yes, %s is PRESENT in the list" %(item)
                return
            else:
                temp = temp.next

        print "No, %s is NOT PRESENT in the list" %(item)

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_node(1)
    LL.printLL()
    LL.add_node(2)
    LL.printLL()
    LL.add_node(3)
    LL.printLL()
    LL.add_node(4)
    LL.printLL()
    LL.add_node(5)
    LL.printLL()
    LL.search(5)
