class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_all(self,data_list):
        if self.head is None:
            for data in data_list:
                self.insert_at_end(data)
            return
        for data in data_list:
            self.insert_at_end(data)
        return

    def length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count


    def remove_at(self,index):
        if index<0 or index>=self.length():
            raise Exception('Invalid index')

        if index==0:
            self.head = self.head.next
            return

        count =0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            count+=1
            itr = itr.next
        return

    def insert_at(self,index,data):
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if itr==index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1
        return



    def insert_after(self, data_after, data_insert):
        if self.head is None:
            self.insert_at_begining(data)
            return
        itr = self.head
        while itr:
            if itr.data==data_after:
                itr.next = Node(data_insert,itr.next)
                break
            itr = itr.next
        return


    def remove_by_value(self,data):
        itr = self.head
        while itr:
            if itr.next.data==data:
                itr.next = itr.next.next
                break
            itr = itr.next



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(89)
    ll.insert_at_end(46)
    ll.print()
    ll.insert_all([8,6,5,4])
    ll.print()
    print(ll.length())
    ll.remove_at(2)
    ll.insert_after(8,7)
    ll.remove_by_value(8)
    ll.print()
    ll.insert_at(2,49)
    ll.print()