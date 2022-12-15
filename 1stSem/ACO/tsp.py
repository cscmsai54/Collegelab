def pathlength(n, adj):
    print("hi")
    visited = []
    non_visited = list(range(0,n))
    print(non_visited)
    


p = []
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
    print("\n")
    print(adj_matrix[i])

    val = pathlength( i , adj_matrix)
    p.append(val)









