from itertools import permutations

#functions 
def shortest(snode, adj):
    subnodes = []
    path = []
    V = len(adj)
    for i in range(V):
        if i != snode:
            subnodes.append(i)
    min_path_cost = 999999
    next_permutation = permutations(subnodes)
    for permutation in next_permutation:
        current_path_cost = 0
        k = snode
        for element in permutation :
            current_path_cost += adj[k][element]
            k = element
        current_path_cost += adj[k][snode]
        if min_path_cost > current_path_cost:
            min_path_cost = current_path_cost
            path = permutation
    return min_path_cost, path

def accept_distance():
    adj_matrix = []
    print("\n\nEnter The Number Of Nodes/Cities :")
    nodes = int(input(">>"))
    print("Enter Distance frome each Nodes : ")
    for i in range (nodes):
        row = []
        for j in range(nodes):
            if i == j :
                v = 0
                row.append(v)
            else :
                print(f"Enter Distance Frome Nodes {i+1} to {j+1}")
                v = int(input(">>"))
                row.append(v)
        adj_matrix.append(row)
    for i in range(0,nodes):
        print(adj_matrix[i])
    print("\n")
    return adj_matrix

#Main block          
adj_matrix = accept_distance()
print("Enter The Starting Node : ")
start1 = int(input(">>")) 
start = start1 - 1
print("\n\nRESULT\n")
finaloutput = shortest(start, adj_matrix )
print(f"Shortest Cost is {finaloutput[0]} \n\nwith path {start1} --->",end=" " ) 
length = len(finaloutput[1])
for i in finaloutput[1] :
    print(f"{i+1} --->",end=" ")    
print(f"{start1} \n")
    














































































