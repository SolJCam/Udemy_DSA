# Binary Search Tree
import pdb

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None  ##
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        entry = Node(value)

        if self.root == None:
            self.root = entry
            return self.root

        start = self.root
        while start.value != None:
            if start.value > value:
                if start.left == None:
                    start.left = entry
                    start.left.parent = start ##
                    return start.left
                else:
                    start = start.left
            else:
                if start.right == None:
                    start.right = entry
                    start.right.parent = start ##
                    return start.right
                else:
                    start = start.right

    def lookup(self, value):
        if self.root.value == value:
            print(f"Root: {value}")
            return self.root
            
        start = self.root
        result = self.__traverse_to_lookup__(start, value)
        print(result)
        return result

    def __traverse_to_lookup__(self, node, value):
        start_node = node

        while start_node.value != None:
            if start_node.value > value:
                if start_node.left.value == value:
                    print(f"Left: {start_node.left.value}")
                    return start_node.left
                elif start_node.left.left == None and start_node.left.right == None:
                    print(f"Left: None")
                    return None
                else:
                    start_node = start_node.left
                    self.__traverse_to_lookup__(start_node, value)
            else:
                if start_node.right.value == value:
                    print(f"Right: {start_node.right.value}")
                    return start_node.right
                elif start_node.right.right == None and start_node.right.left == None:
                    print(f"Right: None")
                    return None
                else:
                    start_node = start_node.right
                    self.__traverse_to_lookup__(start_node, value)

    def remove(self, value):
        root = self.root
        if root.value == value:
            root = root.right
            while root.left != None:
                root = root.left
            left = self.root.left 
            right = self.root.right 
            root.left = left
            root.right = right
            root.parent.left = None ##
            self.root = root    
            print(f"Root: {self.root.value}")
            return self.root.value   

        node = self.lookup_sol(value)
        parent = node.parent
        left = node.left
        right = node.right

        new_node = ''

        if right != None and right.left != None:
            new_node = right.left
            while new_node.left != None:
                new_node = new_node.left
        elif right != None and right.left == None:
            new_node = right
            new_node.parent.right = new_node.right
        elif left != None and left.left != None:
            new_node = left
            while new_node.left != None:
                new_node = new_node.left
        else:
            print(f"No node value {value}")
            return None  
        
        # while new_node.left != None:
        #     new_node = node.left

        if new_node.left == None:
            new_node.parent.left = None

        pdb.set_trace() 
        new_node.left = left
        new_node.right = right
        new_node.parent = parent
            
        node.parent.left = new_node

        print(f"Replacement node: {new_node.value}")
        return node.value 
                 


        # node = self.root        
        # while node != None:
        #     if node.value > value:
        #         node = node.left
        #         # pdb.set_trace()
        #     elif node.value == value:
        #         if node.right == None and node.left == None:
        #             node.parent.left = None
        #             print(f"Replacement node: None")
        #             return node.parent.left  
        #         new_node = node.right
        #         while new_node.left != None:
        #             new_node = new_node.left
        #         # node = new_node  

        #         left = node.left 
        #         right = node.right 
        #         parent = node.parent

        #         new_node.left = left
        #         new_node.right = right
        #         new_node.parent = parent
                 
        #         node.parent.left = new_node
        #         new_node.parent.left = None

        #         print(f"Replacement node: {new_node.value}")
        #         return node.value                 
        #     else:
        #         print(f"No node value {value}")
        #         return None      

                
    # def __traverse__(self, node):
    #     tree = { "value": node.value }
    #     tree["left"] = None if node.left == None else self.__traverse__(node.left)
    #     tree["right"] = None if node.right == None else self.__traverse__(node.right)
    #     return tree


    # Course Solution

    def lookup_sol(self, value):
        if self.root == None:
            print("Empty Tree")
            return None

        node = self.root
        while node != None:
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
            elif node.value == value:
                print(node.value)
                return node
            else:
                print(f"No node value {value}")
                return None



def traverse(node):
    tree = { "value": node.value }
    tree["left"] = None if node.left == None else traverse(node.left)
    tree["right"] = None if node.right == None else traverse(node.right)
    return tree


bst = BST()
# root
bst.insert(11)
#   < root
bst.insert(5)
bst.insert(2)
bst.insert(4)
bst.insert(1)
bst.insert(7)
bst.insert(6)
bst.insert(8)
#   > root
bst.insert(21)
bst.insert(16)
bst.insert(23)
bst.insert(15)
bst.insert(19)
bst.insert(12)
bst.insert(20)
#   remove
# bst.remove(11)
# bst.remove(5)
bst.remove(2)
# bst.remove(4)
# bst.remove(1)
# bst.remove(7)
# bst.remove(6)
# bst.remove(8)
print(traverse(bst.root))
# print(bst.lookup(7))
# print(bst.lookup(11))
# print(bst.lookup(13))
# print(bst.lookup(3))