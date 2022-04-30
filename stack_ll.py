class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        node = Node(data,self.head)
        self.head = node

    def pop(self):
        if self.head is None:
            print('stack is empty')
            return
        self.head = self.head.next
        return

    def print(self):
        if self.head is None:
            print('stack is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)


if __name__=='__main__':
    st = stack()
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