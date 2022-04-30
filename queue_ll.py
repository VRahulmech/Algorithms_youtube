class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
class queue:
    def __init__(self):
        self.head=None

    def push(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return

    def pop(self):
        if self.head is None:
            print('queue is empty')
            return
        self.head = self.head.next
        return

    def print(self):
        itr = self.head
        iitr = ''
        while itr:
            iitr += str(itr.data)+'-->'
            itr = itr.next
        print(iitr)
        return

if __name__=='__main__':
    st = queue()
    st.push(17)
    st.push(3)
    st.print()
    st.pop()
    st.print()
    st.push(34)
    st.print()
    st.pop()
    st.print()
    st.push(21)
    st.print()



