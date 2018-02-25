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
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def delete_node(self, data):
        temp = self.head

        if (temp is not None and temp.data == data):
            self.head = temp.next
            temp = None
            return

        while(temp is not None):
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return

        prev.next = temp.next
        temp = None

    def PrintLL(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next

if __name__=='__main__':

    # Start with the empty list
    meri_LL = LinkedList()
    meri_LL.add_start(5)
    meri_LL.add_start(6)
    meri_LL.add_end(7)
    meri_LL.add_between(meri_LL.head.next,9)
    meri_LL.delete_node(5)
    print 'Created linked list is:',
    meri_LL.PrintLL()
