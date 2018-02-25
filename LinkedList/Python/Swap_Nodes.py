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
        print "Linked list ->",
        while(temp):
            print temp.data,
            temp = temp.next
        print "\n"

    def swap(self,data1,data2):

        if data1 == data2:
            return

        prev_data1 = None
        curr_data1 = self.head
        while curr_data1 is not None and curr_data1.data != data1:
            prev_data1 = curr_data1
            curr_data1 = curr_data1.next

        prev_data2 = None
        curr_data2 = self.head
        while curr_data2 is not None and curr_data2.data != data2:
            prev_data2 = curr_data2
            curr_data2 = curr_data2.next

        if curr_data1 is None or curr_data2 is None:
            return

        if prev_data1 is not None:
            prev_data1.next = curr_data2
        else:
            self.head = curr_data2

        if prev_data2 is not None:
            prev_data2.next = curr_data1
        else:
            self.head = curr_data1

        temp = curr_data1.next
        curr_data1.next = curr_data2.next
        curr_data2.next = temp

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
    LL.swap(1,5)
    LL.printLL()
