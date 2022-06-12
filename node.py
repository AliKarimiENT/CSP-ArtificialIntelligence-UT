class Node():    

    # list of adjacent items 
    
    # value for this node 
    value = 0 
    def __init__(self,shape,id):
        self.shape = shape
        self.id = id
        self.adjacencyList = []
    
    def addAdjcentItem(self,node):
        self.adjacencyList.append(node)
       
    
    def getAdjacencyList(self):
        return self.adjacencyList
    
    def setValue(self,val):
        self.value = val



