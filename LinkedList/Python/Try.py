class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_start(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_between(self,prev_node,new_data):
        if prev_node is None:
            print ("Previous node doesn't exist.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def add_end(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def delete_node(self,item):
        temp = self.head

        if temp is not None and temp.data == item:
            self.head = temp.next
            temp = None
            return

        while temp is not None:
            if temp.data == item:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def printLL(self):
        temp = self.head
        print 'Created linked list is:',
        while(temp):
            print temp.data,
            temp = temp.next
        print '\n'

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_start(5)
    LL.printLL()
    LL.add_end(6)
    LL.printLL()
    LL.add_start(4)
    LL.printLL()
    LL.add_between(LL.head,8)
    LL.printLL()
    LL.delete_node(8)
    LL.printLL()
