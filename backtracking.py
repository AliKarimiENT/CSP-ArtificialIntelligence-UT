from copy import deepcopy
from tkinter import N


class CSPBacktracking:
    def __init__(self,csp):
        self.csp = csp
        self.nodes = deepcopy(csp.nodes)
    

    def isComplete(self):
        nodes = self.csp.nodes
        for node in nodes:
            if node.value == -1:
                return False
        return True
    
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

    def backtrack(self):
        if self.isComplete():
            return True
        node = self.getUnassignedNode(True)
        
        for d in node.domain:
            node.value = d
            self.nodes[node.id].value = d
            self.csp.nodes = self.nodes
            if self.checkNeighbors(node):
                isSuccess = self.forwardChecking(node)
                if isSuccess:
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