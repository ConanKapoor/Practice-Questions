class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def PrintLL(self):
        temp = self.head
        print 'Created linked list is:',
        while(temp):
            print temp.data,
            temp = temp.next
        print '\n'

    def add_start(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def add_between(self,prev_node,new_data):
        if prev_node is None:
            print "Previous node doesn't exist."
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def add_end(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def delete_node(self, item):
        temp = self.head

        if temp is not None and temp == item:
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

    def delete_position(self, position):
        temp = self.head

        if temp == None:
            return
        elif position == 1:
            self.head = temp.next
            temp = None
        else:
            for x in range(0,position-1):
                if temp.next is None:
                    print "Chutiye itni badi to list nahi hai \n"
                    return
                prev = temp
                temp = temp.next
            prev.next = temp.next
            temp = None

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_end(1)
    LL.PrintLL()
    LL.add_end(2)
    LL.PrintLL()
    LL.add_end(3)
    LL.PrintLL()
    LL.add_end(4)
    LL.PrintLL()
    LL.add_end(5)
    LL.PrintLL()
    LL.delete_position(6)
    LL.PrintLL()
