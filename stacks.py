import pdb


#         # Linked List implmentation

# class node:
#     def __init__(self, value):
#         self.data = value
#         self.next = None


# class stack:
#     def __init__(self):
#         self.top = None
#         self.bottom = None
#         self.length = 0


#     def peek(self):
#         return self.length, self.top.data

        
#     def push(self, value):
#         list_item = node(value)

#         if self.length == 0:
#             self.top = list_item
#             self.bottom = list_item
#         else:
#             list_item.next = self.top
#             self.top = list_item

#         self.length += 1
#         # pdb.set_trace()
#         return self.length, self.top.data


#     def pop(self):
#         if self.top != None:
#             self.top = self.top.next
#             self.length -= 1

#             if self.length == 0:
#                 self.bottom = None
#                 return self.length, self.top
                
#             return self.length, self.top.data
#         else:
#             return None



        # Array implmentation

class stack:
    def __init__(self):
        self.container = []


    def peek(self):
        if len(self.container) == 0:
            return None
        else:
            return len(self.container), self.container[len(self.container)-1]

        
    def push(self, value):
        self.container.append(value)
        # pdb.set_trace()
        return len(self.container), self.container[len(self.container)-1]


    def pop(self):
        if len(self.container) != 0:
            # self.container.pop()      
            
            # if len(self.container) == 0:
            #     return len(self.container), self.container[len(self.container)]
            # else:
            #     return len(self.container), self.container[len(self.container)-1]


            # for use in Queues    
            popped = self.container.pop()
            return popped 

        else:
            return None




# import stacks
# stacky = stacks.stack()
# stacky.push("Doku")
# stacky.push("Fati")
# stacky.push("Dembele")
# stacky.push("Camavinga")
# stacky.push("Traore")
# stacky.peek