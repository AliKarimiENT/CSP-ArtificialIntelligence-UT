from copy import deepcopy
from tkinter import N


class CSPBacktracking:
    def __init__(self,csp):
        # defining self variables
        # csp is our input from CSP class
        # nodes are csp's nodes
        self.csp = csp
        self.nodes = deepcopy(csp.nodes)
    

    #* this function will check that setting values completed or not
    # by checking that for each nodes , node's value is equal to -1 or not
    # then return False if value is -1 otherwise True
    def isComplete(self):
        nodes = self.csp.nodes
        for node in nodes:
            if node.value == -1:
                return False
        return True
    
    #* this function is for getting node with value equal to -1 (unassigned value)
    def getUnassignedNode(self, mrv):
        nodes = self.nodes
        min = 20
        minNode = None
        for node in nodes:
            if node.value == -1:
                if not mrv: 
                    return node
                else:
                    length = len(node.domain)
                    if minNode is None:
                        min = length
                        minNode = node
                    else:
                        if length < min:
                            min = length
                            minNode = node
        return minNode

    # checking node's neighbors with checkNodeConstrain() function for nodes with value not equal to -1
    def checkNeighbors(self,node):
        nodes = self.csp.nodes
        hasUnvisitedNode = False
        for neighbor in node.neighborsList:
            value =  nodes[neighbor.id].value
            if value != -1 :
                if not self.csp.checkNodeConstraints(nodes[neighbor.id]):
                    return False
                else:
                    hasUnvisitedNode = True
        if hasUnvisitedNode:
            return True
        else:
            return self.csp.checkNodeConstraints(node)

    # function for checking nodes forward
    # by applying constraints for each shape
    def forwardChecking(self, node):
        if node.shape == 'S':
            self.csp.applySquareConstraints(node)
        elif node.shape == 'P':
            self.csp.applyPentagonConstraints(node)
        elif node.shape == 'T':
            self.csp.applyTriangleConstraints(node)
        elif node.shape == 'H':
            self.csp.applyHexagonConstraints(node)
        elif node.shape == 'C':
            self.csp.applyCircleConstraints(node)
        for node in self.nodes:
            if not node.domain:
                return False
        return True

    # function for resetting domain to initial state
    def resetDomains(self, node,all):
        nodes = self.csp.nodes
        if all:
            for node in nodes:
                node.domain = [i+1 for i in range(9)]
            return
        for neighbor in node.neighborsList:
            if len(nodes[neighbor.id].domainHistory) > 1:
                nodes[neighbor.id].domainHistory.pop()
            nodes[neighbor.id].domain = deepcopy(nodes[neighbor.id].domainHistory[len(nodes[neighbor.id].domainHistory)-1])

    # main function for running processes
    def backtrack(self):
        # check if nodes became complete or not
        if self.isComplete():
            return True
        # get an unassigned node
        node = self.getUnassignedNode(True)
        
        # set different values from domain and check neighbors and other processes
        for d in node.domain:
            node.value = d
            self.nodes[node.id].value = d
            self.csp.nodes = self.nodes
            if self.checkNeighbors(node):
                # if checking neighbors doesn't have any problem and returned True
                # use forwardChecking()
                isSuccess = self.forwardChecking(node)
                # if isSuccess type is True
                if isSuccess:
                    # call backtrack 
                    result = self.backtrack()
                    if result != False:
                        return True
                    self.resetDomains(node,False)
        node.value = -1
        self.nodes[node.id].value = -1
        self.csp.nodes = self.nodes
        self.resetDomains(node,False)
        return False
                

    def run(self):
        self.backtrack()
        for node in self.csp.nodes:
            print(node.value)
        print('----------------- CSP Check Result ----------------')
        print(self.csp.checkWholeNodes())