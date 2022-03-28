# Binary Search Tree
import pdb

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None ##
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
        old_node = self.lookup_sol(value)
        if old_node == None:
            print(f"No node value {value}")
            return None

        new_node = value + 1
        exists = ''
        while new_node != None:
            exists = self.lookup_sol(new_node)
            if exists != None:
                new_node = None
            else:
                new_node += 1

        new_node_parent = exists.parent
        pdb.set_trace()
        if new_node_parent.left != None:
            if new_node_parent.left.value == exists.value:
                new_node_parent.left = exists.left
        if new_node_parent.right != None:
            if new_node_parent.right.value == exists.value:
                new_node_parent.right = exists.right

        left = old_node.left
        right = old_node.right
        exists.left = left
        exists.right = right 
        if old_node.parent != None:
            parent = old_node.parent
            if parent.left != None:
                if parent.left.value == old_node.value:
                    parent.left = exists
            if parent.right != None:
                if parent.right.value == old_node.value:
                    parent.right = exists
            exists.parent = parent
        else:
            exists.parent = None
            self.root = exists

        print(f"Replacement node: {exists.value}")
        return exists.value

                
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
# bst.remove(2)
# bst.remove(4)
# bst.remove(1)
# bst.remove(7)
# bst.remove(6)
bst.remove(8)
# bst.remove(21)
# bst.remove(16)
# bst.remove(23)
# bst.remove(15)
# bst.remove(19)
# bst.remove(12)
# bst.remove(10)
print(traverse(bst.root))
# print(bst.lookup(4))
# print(bst.lookup(7))
# print(bst.lookup(11))
# print(bst.lookup(13))
# print(bst.lookup(3))