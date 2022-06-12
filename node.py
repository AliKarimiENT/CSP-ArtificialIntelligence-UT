class Node():    

    # list of adjacent items 
    adjacencyList = []
    # value for this node 
    value = 0 
    def __init__(self,shape,id):
        self.shape = shape
        self.id = id

    
    def addAdjcentItem(self,node):
        adjacencyList.append(node)
       
    
    def getAdjacencyList(self):
        return self.adjacencyList
    
    def setValue(self,val):
        self.value = val



