
# first getting the inputs
# t is tests count
from backtracking import CSPBacktracking
from csp import CSP
from edge import Edge
from node import Node



t = input("Enter tests count :\n") 

# v is variable for nodes count , e is for number of graph edges
ev_text_input = input("Enter value for V and E : ex.(2 1)\n")
v = int(ev_text_input.split(" ",1)[0])
e = int(ev_text_input.split(" ",1)[1])



# enter chars for each node
chars_input = input("Enter chars list for each node \n")
chars = chars_input.split(" ")

# generate nodes list 
nodes = []
for i in range(v):
    nodes.append(Node(chars[i],i))

# list of edges between nodes
print("Enter pair edge numbers ")
edges = []

for i in range(e):
    edge =  input()+"\n"
    edges_arr = edge.split()
    v0 = next(node for node in nodes if node.id==int(edges_arr[0]))
    v1 = next(node for node in nodes if node.id==int(edges_arr[1]))

    edges.append(Edge(v0,v1)) 



# initial all adjacency items
for n in nodes:
    for ed in edges:
        if n.id == ed.n0.id :
            if ed.n1 is not n:
                n.addNeighborItem(ed.n1)
        elif n.id == ed.n1.id:
            if ed.n0 is not n:
                n.addNeighborItem(ed.n0)
           
print(chars)
# print(edges)

csp = CSP(nodes)
cspSolver = CSPBacktracking(csp)
cspSolver.run()

