from copy import deepcopy
import string


class CSP:

    def __init__(self, nodes):
        # getting list of nodes in the graph
        self.nodes = nodes

    #* final step of processes is checkWholeNodes()
    # with this function we check node constraints for each node 
    # if the result of checkNodeConstraints() was True , it means that we have successfully done the process
    # else the result be False , means that our result has problems
    def checkWholeNodes(self):
        for node in self.nodes:
            if not self.checkNodeConstraints(node):
                return False
        return True

    #* function for checking node's constraints 
    # function's input is our node in the graph
    def checkNodeConstraints(self, node):
        # constraint is variable for storing value for the node with calculateConstraintValue function
        # inputs of calculateConstraintValue() function are list of neighbors , summation / multiply and side of selected char in the calculation
        constraint = 0
        # for each type of shapes for each node we calculate constraint value
        if node.shape == 'P': #* Shape is Pentagon
            # for type P 
            # the constraint value is equal to the leftmost digit of the sum of the numbers attributed to the adjacent nodes
            constraint = self.calculateConstraintValue(node.neighborsList,'summation','left')
        elif node.shape == 'H': #* Shape is Hexagonal
            # for type H
            # the constraint value is equal to the rightmost digit of the sum of the numbers attributed to adjacent nodes
            constraint = self.calculateConstraintValue(node.neighborsList,'summation','right')
        elif node.shape == 'S': #* Shape is Square
            # for type S
            # the constraint value is equal to the rightmost digit of the digit multiplied by the numbers assigned to its adjacent nodes
            constraint = self.calculateConstraintValue(node.neighborsList,'multiply','right')
        elif node.shape == 'T': #* Shape is Triangle
            # for type T
            # the constraint value is equal to the leftmost digit of the digit multiplied by the numbers assigned to its adjacent nodes
            constraint = self.calculateConstraintValue(node.neighborsList,'multiply','left')
        elif node.shape == 'C': #* Shape is Circle
            return True
        if node.value == constraint or constraint is None:
            return True
        return False

    #* Function for calculating constraint value
    def calculateConstraintValue(self, neighbors,type,alignment): 
        # inputs : neighbors > list of neighbors , type : multiply / summation , alignment : right / left
        acc = 0
        if type == 'multiply':
            acc = 1
        for neighbor in neighbors:
            if self.nodes[neighbor.id].value == -1:
                return None
            if type == 'summation':
                acc += self.nodes[neighbor.id].value
            elif type == 'multiply' :
                acc *= self.nodes[neighbor.id].value
        if alignment == 'left':
            return int(str(acc)[0])
        elif alignment == 'right':
            value = str(acc)
            return int(value[len(value)-1])

    #* applyUnitConstraint() function
    # this function is usable for nodes with neighbors list with only 1 item
    # it will manage the domain of the neighbor node
    def applyUnitConstraint(self, node):
        value = node.value
        if len(node.neighborsList) == 1:
            neighbor = node.neighborsList[0]
            domain = deepcopy(self.nodes[neighbor.id].domain)
            revised = False
            for d in domain:
                if d != value:
                    self.nodes[neighbor.id].domain.remove(d)
                    revised = True
                if revised:
                    if domain != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        self.nodes[neighbor.id].domainHistory.append(domain)


    # -------------------------------------------------------------------------------------------------
    # below functions are for applying constraints for different types
    def applySquareConstraints(self, node):
        value = node.value
        if value in [1,3,5,7,9]:
            for neighbor in node.neighborsList:
                domain = deepcopy(self.nodes[neighbor.id].domain)
                revised = False
                for d in self.nodes[neighbor.id].domain:
                    if d==2 or d==4 or d==6 or d==8:
                        self.nodes[neighbor.id].domain.remove(d)
                        revised = True
                    if revised:
                        if domain != [1,2,3,4,5,6,7,8,9]:
                            self.nodes[neighbor.id].domainHistory.append(domain)
        self.applyUnitConstraint(node)
    
    def applyPentagonConstraints(self, node):
        self.applyUnitConstraint(node)

    def applyTriangleConstraints(self, node):
        self.applyUnitConstraint(node)

    def applyHexagonConstraints(self, node):
        self.applyUnitConstraint(node)

    def applyCircleConstraints(self, node):
        self.applyUnitConstraint(node)