

def add(towhat,newquay,where):
        info = towhat.get(newquay,[])
        info.append(where)
        towhat[newquay] = info
        
    

def visited_func(n):
    #n = int(input("enter number of nodes in graph"));
    visited = {}
    print(n)
    for i in range (1,n+1):
        visited[i]=0


def DFS(alternate):
    stack = []
    visited={}
    for i in alternate:
        visited[i]=0
        print(i, visited[i])
    s=input("enter the first node frome where u wanna start")
    stack.append(s);
    while stack:
        v = stack.pop()
        if(visited[v]==0):
            visited[v]=1
            print(v)
        
        for a in alternate[v]:
            if(visited[a]==0):
                stack.append(a)
        
            
            
                
                
                
            
        
            
        
 
    
    
    

    
alternate={}   
#count=0
while True:
    ch=input("do u wish to continue")
    if ch=='0':
        key=input("enter start key")
        value=input("enter end key")
        add(alternate,key,value)
        add(alternate,value,key)
        #count=count+1
        print(alternate)
    elif ch=='1':
        #visited_func(count)
        DFS(alternate)
    elif ch=='3':
        break
        
   




    