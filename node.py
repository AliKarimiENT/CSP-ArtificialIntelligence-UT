class Node():    

    # list of adjacent items 
    
    # value for this node 
    
    def __init__(self,shape,id):
        self.shape = shape
        self.id = id
        self.neighborsList = []
        self.value = -1 
        self.domain = [i+1 for i in range(9)]
        self.domainHistory = [[i+1 for i in range(9)]]

    def addNeighborItem(self,node):
        self.neighborsList.append(node)
       
    
    def getNeighborsList(self):
        return self.neighborsList
    
    def setValue(self,val):
        self.value = val
    
    def getValue(self):
        return self.value



