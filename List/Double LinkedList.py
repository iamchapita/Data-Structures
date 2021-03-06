# -*- coding: utf-8 -*-

# @author: iamchapita
# @version: 0.1.0
# @date: 2021/05/06

from Node import Node

class Double_LinkedList:

    def __init__(self):
        self.first = None

    def push(self, value, position = 0):

        if(not isinstance(position, int) or position < 0 or position > self.length()):
            return False
        
        #Caso base: si no hay ningun elemento (nodo) en la lista
        if(not self.first):
            self.first = Node(value)
            return True
        
        #Caso 1: agregando un elemento (nodo) en la primer posición
        if(position == 0):
            current = self.first
            self.first = Node(value)
            self.first.next = current
            self.first.next.prev = self.first    
            return True
        
        before = self.first
        current = self.first.next
        count = 1
        
        #Caso 2: agregando un elemento (nodo) en cualquier posición que no sea la primera
        while (before):
            
            if(count == position):

                before.next = Node(value)
                before.next.prev = before    
                before.next.next = current
                return True

            count += 1
            before = before.next
            current =  current.next

        current = Node(value)
        return True

    def print(self, order = "up"):

        current = self.first
        string = ""

        #Imprimir en orden ascendente
        if(order == "up"):

            while(current):

                string += (("%s <=> ")%(current.value))
                current = current.next
            
            string += "null"
            print(string)
        
        #Imprimir en orden descendente
        elif(order == "down"):
    
            while(current):

                if(current.next == None):
                    break

                current = current.next
        
            while (current):

                string += (("%s <=> ")%(current.value))
                current = current.prev
                
            string += "null"
            print(string)

    def delete(self, position):
        
        if(not isinstance(position, int) or position < 0 or position > self.length()):
            return False

        if(position == 0):
            self.first = self.first.next
            self.first.prev = None
            return True
        
        count = 1
        before = self.first
        current = self.first.next
        
        while (current):

            if(count == position):

                before.next = before.next.next
                before.next.prev = current.prev
                return True
            
            count += 1
            before = before.next
            current =  current.next
        
        return False

    def search(self, value):

        current = self.first

        while (current):
            
            if(value == current.value):
                print(True)
                return True

            current =  current.next
        
        print(False)
        return False

    def length(self):
        
        current = self.first
        count = 0

        while (current):

            count += 1    
            current = current.next
        
        return count

    
Dll = Double_LinkedList()
Dll.push(1,0)
Dll.push(2,1)
Dll.push(3,2)
Dll.push(4,3)
Dll.push(5,4)
Dll.push(6,5)
Dll.push(7,6)
Dll.push(8,7)
Dll.push(9,8)

Dll.print("up")
Dll.print("down")

Dll.delete(4)
Dll.print("up")

