# -*- coding: utf-8 -*- 
from LinkedList import LinkedList

class Node:

    def __init__(self, value):

        self.value =  value
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root =  None

    def add(self, value):
        current = self.root
        self.addInner(value, current)

    def addInner(self, value, current):

        if(current == None):
            self.root = Node(value)
            return True

        if(isinstance(current, Node)):

            if(current.value > value):

                if(not current.left):

                    current.left = Node(value)
                    return True

                else: return self.addInner(value, current.left)

            else:

                if(not current.right):

                    current.right = Node(value)
                    return True
                
                else: return self.addInner(value, current.right)

    def convert(self, linkedlist):

        if(not isinstance(linkedlist, LinkedList)): return False
        
        current = linkedlist.first
        
        while (current):
            
            value = current.value
            self.add(value)
            current = current.next
        
        return True

    def search(self, value):
        current = self.root
        self.searchInner(value, current)

    def searchInner(self, value, current):

        if(not current): 
            return False

        if(current.value == value): 
            print(current.value)

        else:

            if(current.value > value): 

                if(not current.left): 
                    return False
                
                return self.searchInner(value, current.left)

            else:

                if(not current.right): 
                    return False
                
                return self.searchInner(value, current.right)
    
    def print(self):
        current = self.root
        self.printInner(current, 0)

    def printInner(self, current, space) : 

        if (current == None): 
            return False
        
        space += 7

        self.printInner(current.right, space)  
        print()  
        
        for i in range(space): 
            print(end = " ")  

        print(current.value)  
  
        self.printInner(current.left, space)  
        

bst = BST()

bst.add(1)
bst.add(10)
bst.add(11)
bst.add(12)
bst.add(-4)
bst.add(-3)
bst.add(8)
bst.add(-7)
bst.add(-1)
bst.add(4)
bst.add(7)
bst.add(5)

#bst.search(-7)

#bst.print()


#======================================================================================#

ll = LinkedList()
ll.push(10,0)
ll.push(15,1)
ll.push(29,2)
ll.push(33,3)
ll.push(49,4)
ll.push(46,5)
ll.push(60,6)
ll.push(38,7)
ll.push(110,8)
ll.push(66,6)
ll.push(9,9)
ll.push(5,10)
ll.push(3,11)
ll.push(4,12)
ll.push(7,13)
ll.push(11,14)
ll.push(1,15)

bst1 = BST()

#bst1.convert(ll)

#bst1.print()





