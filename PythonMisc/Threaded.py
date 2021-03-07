class Node:
    def __init__(self,value):
        self.value = value
        self.Left = self.Right = None
        self.lth = self.rth = 1

def Insert(root,temp):
    if(temp.value < root.value):
        if(root.lth == 1):
            temp.Left = root.Left
            temp.Right = root
            root.Left = temp
            root.lth = 0
        else:
            Insert(root.Left,temp)
    elif(temp.value > root.value):
        if(root.rth == 1):
            temp.Right = root.Right
            temp.Left = root
            root.Right = temp
            root.rth = 0
        else:
            Insert(root.Right,temp)


def Inorder(temp,headernode):
    while(temp != headernode):
        while(temp.lth == 0):
            temp = temp.Left
        print(temp.value,end = "  ")
        while(temp.rth == 1):
            temp = temp.Right
            if(temp == headernode):
                break
            print(temp.value,end = "  ")
        temp = temp.Right


def Preorder(temp,headernode):
    while(temp != headernode):
        print(temp.value,end="  ")
        while(temp.lth == 0):
            temp = temp.Left
            print(temp.value,end="  ")
        while(temp.rth == 1):
            temp = temp.Right
            if(temp == headernode):
                break
        temp = temp.Right


root = hNode = None
hNode = Node("999")
print("\t\tTHREADED BINARY TREE.....\nOPERATIONS : ")
print("1. INSERTING DATA\n2. INORDER TRAVERSAL\n3. PREORDER TRAVERSAL\n4. EXIT")
while True:
    choice = int(input("PLEASE ENTER YOUR CHOICE : "))
    if(choice == 1):
        value = int(input("Enter the value : "))
        temp = Node(value)
        if root is None:
            root = temp
            hNode.Left = root
            hNode.Right = hNode
            root.Left = hNode
            root.Right = hNode
        else:
            Insert(root,temp)
    elif(choice == 2):
        print("INORDER TRAVERSAL : ")
        Inorder(root,hNode)
        print()
    elif(choice == 3):
        print("PREORDER TRAVERSAL : ")
        Preorder(root,hNode)
        print()
    elif(choice == 4):
        print("EXIT!!!")
        break
    else:
        print("PLEASE ENTER A VALID OPTION!!!")