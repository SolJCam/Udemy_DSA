import pdb

class singly_linked_list:
    def __init__(self, value):
        self.head = {
            "data": value,
            "next": None
        }
        
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            "data": value,
            "next": None
        }

        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

        return self.head

    def prepend(self, value):
        new_node = {
            "data": value,
            "next": self.head
        }
        
        self.head = new_node
        self.length += 1

        return self.head

    def insert(self, value, index):
        if index > self.length:
            self.append(value)
        
        new_node = {
            "data": value,
            "next": None
        } 

        node = self.head
        counter = 1

        while counter < index:
            if index != 0:
                node = node["next"]
                counter += 1
            else:
                self.prepend(value)

        next_node = node["next"]
        node["next"] = new_node
        node["next"]["next"] = next_node
        self.length += 1
        
        return self.head

    def remove(self, index):
        node = self.head
        counter = 1

        while counter < index:
            if index != 0:
                node = node["next"]
                counter += 1

        next_node = node["next"]["next"]
        node["next"] = next_node
        self.length -= 1        

        return self.head


        # Course Answer
    def reverse(self):
        if self.head["next"] == None:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next

        while second != None:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head.next = None
        self.head = first

        return self.head





# import linked_list
# ll = linked_lists.singly_linked_list("Dembele")
# ll = linked_lists.doubly_linked_list("Dembele")
# ll.append("Camavinga")
# ll.append("Traore")
# ll.append("Doku")
# ll.insert("Fati", 2)




class doubly_linked_list:
    def __init__(self, value):
        self.head = {
            "data": value,
            "next": None,
            "prev": None
        }
        
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = {
            "data": value,
            "next": None,
            "prev": None
        }

        new_node["prev"] = self.tail
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1

        return self.head

    def prepend(self, value):
        new_node = {
            "data": value,
            "next": None,
            "prev": None
        }
        
        new_node["next"] = self.head
        self.head["prev"] = new_node
        self.head = new_node
        self.length += 1

        return self.head

    def insert(self, value, index):
        if index > self.length:
            self.append(value)
        
        new_node = {
            "data": value,
            "next": None,
            "prev": None
        } 
           
        node = self.head
        counter = 1

        while counter < index:
            if index != 0:
                node = node["next"]
                counter += 1
            else:
                self.prepend(value)

        next_node = node["next"]
        prev_node = node
        prev_node["next"] = new_node
        new_node["prev"] = prev_node
        new_node["next"] = next_node
        next_node["prev"] = new_node

        self.length += 1
        
        return self.head

    def remove(self, index):

        node = self.head
        counter = 1

        while counter < index:
            if index != 0:
                node = node["next"]
                counter += 1

        next_node = node["next"]["next"]
        node["next"] = next_node
        next_node["prev"] = node
        self.length -= 1        

        return self.head