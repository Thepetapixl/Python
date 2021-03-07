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

while True:
    ch = input("Do u wish to continue? Press 0 for continuation")
    if ch == '0':
        key = input("Enter start key")
        value = input("Enter end key")
        edge = input("Enter the edge")
        add(alternate,key,value)
        add(alternate,value,key)
        print(alternate)
    elif ch=='1':
        #visited_func(count)
        DFS(alternate)
    elif ch=='3':
        break
        