from collections import defaultdict
count = 0 

#Global variable count to keep a track of table's load Factor to
 #80% or 75%(as per the users choice)
# Class declaration and definitions starts here
 
class HashTable:
 # initializing the dictionary values by -1
 def __init__(self,size):
     self.hashTab = defaultdict().fromkeys(range(size), -1)

 # Function to calculate hash value using MODULO method
 def hashing(self,key):
     return ( key % size )
 
 # Function demonstrating Linear Probing without replacement
 def woreplace(self,key,pos):
     global count
     if self.hashTab[pos] == -1: #pos is vacant in the hashtable
         self.hashTab[pos] = key #Place the key at its home address
         count = count + 1 #Increase the count by 1
     else: # Collison: Search linearly down for the vacant position
         self.find_next_vacant_pos(key,pos)

# Function to handle collision
 def find_next_vacant_pos(self,key,pos):
     global count
     for i in range(1,size):
         z = (pos+i) % size # (hash(key) + i) % M; i is 1 to M-1
         if self.hashTab[z] == -1: # Vacant position
             self.hashTab[z] = key # Key placement at new vacant position
             count = count + 1 # Increase the count by 1
             break
         # Function demonstrating Linear Probing with replacement
 def wreplace(self,key,pos):
    global count
    if self.hashTab[pos] == -1: #pos is vacant in the hashtable
        self.hashTab[pos] = key #Place the key at home address
        count = count + 1 #Increase the count by 1
    elif pos == self.hashing(self.hashTab[pos]): #The existing value is at
                #its home address
        self.find_next_vacant_pos(key,pos) #Search Linearly down
    else: #The existing value is NOT at its home address
        temp = self.hashTab[pos] # Remove the existing record and
                    # store it in temp var
        self.hashTab[pos] = key # Place the key AT ITS PROPER POSITION
        self.find_next_vacant_pos(temp,pos) # Re-store the existing record at
                    # next VACANT POSITION

 # Function to display the hash table
 def display(self):
     print("****** Hash Table *****")
     for i in self.hashTab.items():
         print(i)
         1
         # Function to perform search in the hash table
 def search(self,key):
     flag = 0
     pos = self.hashing(key) #Calculate the position using MODULO
     if self.hashTab[pos] == key: #Key resides at its home address
         print (str(key) +" found at its home address !!")
     else: #Search linearly down the table
         for i in range(1,size):
             z = (pos+i) % size # (hash(key) + i) % M
             if self.hashTab[z] == key: # Key found at location z
                 print (str(key) +" found at address " + str(z))
                 flag = 1
                 break
             if flag == 0:
                 print (str(key) + " not present in the Hash table")

#MAIN PROGRAM STARTS HERE
print("COLLISION HANDLING")
size = int(input("Enter the table size: "))#Hash table size
while 1:
    print ("1:Without Replacement\n2:With Replacement\n3:Display\n4:Search\n5:Exit")
    ch = int(input("Enter the option: "))
    if ch == 1: #Linear Probing without replacement
        h = HashTable(size) #Initialize the hash table
        count=0 #reinitialize the count to track the hashtable availability
        while True:
            key = int(input("Enter the key: ")) #Accept the key
            pos = h.hashing(key) #Modulo hash function
            h.woreplace(key,pos) #Call the function
            h.display() #Display the created table
            opt = int(input("Do you want to add more elements:(1 for yes/ 0 for no) "))
            if opt == 1: #User wish to add more elements
                if (count * 100 / size) >= 80: #But Hash table is 80% full
                    print("Hash Table is nearly full!! Cannot add more elements")
                    break;
                else: #User doesn't wish to add more elements
                    break
            elif ch == 2: #Linear Probing with replacement
                h = HashTable(size) #Initialize the hash table
                count=0 #reinitialize the count to track the hashtable availability
            while True:
                key = int(input("Enter the key: ")) #Accept the key
                pos = h.hashing(key) #Modulo hash function
                h.wreplace(key,pos) #Call the function
                h.display() #Display the created table
                opt = int(input("Do you want to add more elements:(1 for yes/ 0 for no) "))
                if opt == 1: #User wish to add more elements
                    if (count * 100 / size) >= 80: #But Hash table is 80% full
                        print("Hash Table is nearly full!! Cannot add more elements")
                        break;
                    else: #User doesn't wish to add more elements
                        break
                elif ch == 3:
                    print("\n")
                    h.display()
                    2
                elif ch == 4:
                    id = int(input("Enter the key value to be searched: "))
                    h.search(id)
                else:
                    break