graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
  }
visited = []
queue = []  
def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)
  while queue:          # Creating loop to visit each node
    element = queue.pop(0) 
    print (element, end = ",") 
    for next in graph[element]:
      if next not in visited:
        visited.append(next)
        queue.append(next)
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling