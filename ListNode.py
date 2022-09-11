class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Answer:
    def mergeTwoLists(self, a, b):
        return

    def push(head_ref, new_data):
  
    # Allocate node 
        new_node = ListNode()
   
    # Put in the data  
        new_node.val  = new_data
   
    # Link the old list off the 
    # new node 
        new_node.next = (head_ref)
   
    # Move the head to point to 
    # the new node 
        (head_ref) = new_node
        return head_ref
  
# Function to merge two sorted linked lists
# LL1 and LL2 without using any extra space.
    def mergeLists(a, b):
  
    # Run till either one of a 
    # or b runs out
        while (a and b):
  
        # For each element of LL1, compare
        # it with first element of LL2.
            if (a.val > b.val):
      
            # Swap the two elements involved
            # if LL1 has a greater element
                a.val, b.val = b.val, a.val
   
                temp = b
   
            # To keep LL2 sorted, place first
            # element of LL2 at its correct place
                if (b.val and b.val > b.next.val):
                    b = b.next
                    ptr = b
                    prev = None
                  
                # Find mismatch by traversing the
                # second linked list once
                    while (ptr and ptr.val < temp.val):
                        prev = ptr
                        ptr = ptr.next
          
                # Correct the pointers
                    prev.next = temp
                    temp.next = ptr
          
        # Move LL1 pointer to next element
            a = a.next
      
# Function to print the linked link
    def printList(head):
        while (head):
            print(head.val, end = '->')
            head = head.next
      
        print('NULL')
      
# Driver code
    if __name__=='__main__':    
        a = None
        a = push(a, 10)
        a = push(a, 8)
        a = push(a, 7)
        a = push(a, 4)
        a = push(a, 2)
   
        b = None
        b = push(b, 12)
        b = push(b, 3)
        b = push(b, 1)
   
        mergeLists(a, b)
   
        print("First List: ", 
               end = '')
        printList(a)
   
        print("Second List: ", 
               end = '')
        printList(b)





#Описание класса-узла
#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next


class Answer:
    #def mergeTwoLists(self, a, b):
    
    def push(head_ref, new_data):
        new_node = ListNode()
   
    # Put in the data  
        new_node.val  = new_data
   
    # Link the old list off the 
    # new node 
        new_node.next = (head_ref)
   
    # Move the head to point to 
    # the new node 
        (head_ref) = new_node
        return head_ref
  
# Function to merge two sorted linked lists
# LL1 and LL2 without using any extra space.
    def mergeTwoLists(self, a, b):
  
    # Run till either one of a 
    # or b runs out
        while (a and b):
  
        # For each element of LL1, compare
        # it with first element of LL2.
            if (a.val > b.val):
      
            # Swap the two elements involved
            # if LL1 has a greater element
                a.val, b.val = b.val, a.val
   
                temp = b
   
            # To keep LL2 sorted, place first
            # element of LL2 at its correct place
                if (b.val and b.val > b.next.val):
                    b = b.next
                    ptr = b
                    prev = None
                  
                # Find mismatch by traversing the
                # second linked list once
                    while (ptr and ptr.val < temp.val):
                        prev = ptr
                        ptr = ptr.next
          
                # Correct the pointers
                    prev.next = temp
                    temp.next = ptr
          
        # Move LL1 pointer to next element
            a = a.next
      
# Function to print the linked link
    def printList(head):
        while (head):
            print(head.val, end = '->')
            head = head.next
      
        print('NULL')