graph = {
  '5' : ['3','7'],
  '3' : ['2', '4', '5'],
  '7' : ['5','8'],
  '2' : ['3'],
  '4' : ['3','8'],
  '8' : ['4','7']
  }

visited = []
queue = []  

def bfs(visited, graph, node): 
  visited.append(node)
  queue.append(node)
  while queue:        
    print("visited : ",visited)
    print ("queue : ",queue)  
    
    element = queue.pop(0) 
    print (element, end = ",") 
    for next in graph[element]:
      if next not in visited:
        visited.append(next)
        queue.append(next)
        
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    