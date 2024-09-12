graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
    }
visited=[]
queue=[]
node='A'
visited.append(node)
queue.append(node)
while queue:
    s=queue.pop(0)
    print(s,end=" ")
    for neighbour in graph[s]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
