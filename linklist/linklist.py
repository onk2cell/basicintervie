# datastructure linkedlist 

class node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class Linlist:
    def __init__(self):
        self.start = None
    def ViewList(self):
        if self.start == None:
            print("List is Empty")
        else :
            temp = self.start
            while temp != None:
                print(temp.data ,end = " ")
                temp = temp.next

    def addtoend(self,valve):
        Newnode = node(valve)
        if self.start == None:
            self.start = Newnode
        else :
            temp = self.start 
            while temp.next != None :
                temp = temp.next
            temp.next = Newnode
    def delfirst(self):
        if self.start == None:
            print("List is empty")
        else :
             self.start = self.start.next

mylist = Linlist()
mylist.addtoend(2)
mylist.addtoend(0)
mylist.addtoend(2)
mylist.addtoend(20)
mylist.addtoend(0)
mylist.addtoend(210)
mylist.delfirst()
mylist.ViewList()
input("")

