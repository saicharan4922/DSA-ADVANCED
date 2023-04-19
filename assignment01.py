
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
        
    def display(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print()
def delete_zero_sum_sublists(llist):
    if not llist.head:
        return llist
    sum_table = {}
    curr_sum = 0
    curr_node = llist.head
    while curr_node:
        curr_sum += curr_node.data
        if curr_sum == 0:
            llist.head = curr_node.next
            sum_table = {}
        elif curr_sum in sum_table:
            prev_node = sum_table[curr_sum].next
            sum_value = curr_sum + prev_node.data
            while sum_value != curr_sum:
                del sum_table[sum_value]
                prev_node = prev_node.next
                sum_value += prev_node.data
            sum_table[curr_sum].next = curr_node.next
        else:
            sum_table[curr_sum] = curr_node
        curr_node = curr_node.next
    return llist
llist = LinkedList()
llist.append(6)
llist.append(-6)
llist.append(8)
llist.append(4)
llist.append(-12)
llist.append(9)
llist.append(8)
llist.display() # 6 -6 8 4 -12 9 8 
delete_zero_sum_sublists(llist)
llist.display() # 9 8 
