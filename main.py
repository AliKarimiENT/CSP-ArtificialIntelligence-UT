
# first getting the inputs
# t is tests count
t = input("Enter tests count :\n") 

# v is variable for nodes count , e is for number of graph edges
ev_text_input = input("Enter value for V and E : ex.(2 1)\n")
v = int(ev_text_input.split(" ",1)[0])
e = int(ev_text_input.split(" ",1)[1])


# enter chars for each node
chars_input = input("Enter chars list for each node \n")
chars = chars_input.split(" ")

# list of edges between nodes
print("Enter pair edge numbers ")
edges = []
for i in range(e):
    edge =  input()+"\n"
    edges.append(edge.split())

print(chars)
print(edges)