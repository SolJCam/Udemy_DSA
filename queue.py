import pdb
from stacks import stack


#         #Linked List implmentation

# class node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None


# class queue:
#     def __init__(self):
#         self.first = None
#         # self.last = None
#         self.length = 0


#     def peek(self):
#         return self.length, self.first.data

        
#     def enqueue(self, value):
#         joined_line = node(value)

#         if self.length == 0:
#             self.first = joined_line
#             # self.last = joined_line
#         else:
#             in_line = self.first

#             while in_line.next != None:
#                 in_line = in_line.next

#             in_line.next = joined_line

#             # self.last.next = joined_line
#             # self.last = joined_line

#         self.length += 1
#         # pdb.set_trace()
#         return self.length, self.first.data


#     def dequeue(self):
#         if self.first != None:
#             self.first = self.first.next
#             self.length -= 1

#             if self.length == 0:
#                 return self.length, self.first
                
#             return self.length, self.first.data
#         else:
#             return self.length, self.first

#         # if self.length == 0:
#         #     return self.length, self.first

#         # if self.first != None:
#         #     self.first = self.first.next
#         #     self.length -= 1

#         #     return self.length, self.first.data



# import queue
# queuey = queue.queue()
# queuey.enqueue("Fati")
# queuey.enqueue("Doku")
# queuey.enqueue("Dembele")
# queuey.peek()
# queuey.dequeue()




#         #Stack implmentation

class queue:
    def __init__(self):
        self.first = None
        self.container = stack()
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        if self.length == 0:
            self.first = value

        self.container.push(value)
        self.length += 1
        
        return self.peek(), self.length

        # if self.first.peek() == None:
        #     self.first = value

        # self.last.push(value)
        # self.length += 1
        # return self.first, self.length

    def dequeue(self):

        if self.first == None:
            return "No items in queue"

        inverted_queue = stack()
        while self.container.peek() != None:
            inverted_queue.push(self.container.pop())
        
        popped = inverted_queue.pop()
        # pdb.set_trace()
        if inverted_queue.peek() != None:
            self.first = inverted_queue.peek()[1]
        else:
            self.first = None
            return "Removed :"+popped+", first: None"
        
        while inverted_queue.peek() != None:
            self.container.push(inverted_queue.pop())

        return "Removed :"+popped+", first: "+self.first