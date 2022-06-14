from copy import deepcopy
import string


class CSP:

    def __init__(self, nodes):
        self.nodes = nodes


    def checkWholeNodes(self):
        for node in self.nodes:
            if not self.checkNodeConstraints(node):
                return False
        return True

    def checkNodeConstraints(self, node):
        constraint = 0
        if node.shape == 'P':
            constraint = self.calculateConstraintValue(node.neighborsList,'summation','left')
        elif node.shape == 'H':
            constraint = self.calculateConstraintValue(node.neighborsList,'summation','right')
        elif node.shape == 'S':
            constraint = self.calculateConstraintValue(node.neighborsList,'multiply','right')
        elif node.shape == 'T':
            constraint = self.calculateConstraintValue(node.neighborsList,'multiply','left')
        elif node.shape == 'C':
            return True
        if node.value == constraint or constraint is None:
            return True
        return False


    def calculateConstraintValue(self, neighbors,type,alignment):
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