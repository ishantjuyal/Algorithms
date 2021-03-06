"""
Program for Nth node from the end of a Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = "-> ")
            temp = temp.next
        print("NULL")
    
    # Iterative approach
    def get_length(self):
        count = 0 # Initiate a count

        temp = self.head
        while temp: # Traverse through the Linked List
            count += 1 # Change the count to know how many nodes have been counted
            temp = temp.next
        return(count)
    
    def getNth(self, n):
        count = 0 # Initiate a count to keep check on how many nodes we have covered

        temp = self.head
        while temp:
            if count == n: # If the count is same as index needed, return the data from that node
                return(temp.data)
            count += 1 # In case this is not the node, increase the count.
            # We increase count after loop because index starts from 0
            temp = temp.next

if __name__ == '__main__':
 
    # Start with the empty list 
    llist = LinkedList() 
    
    for i in range(5, 0, -1):
        llist.push(i)
    
    llist.printList()
    length = llist.get_length()

    n = length//2

    print("Middle of Linked List is :", llist.getNth(n))