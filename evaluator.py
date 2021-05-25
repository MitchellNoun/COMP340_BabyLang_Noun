#Author: Mitchell Noun
#Date: 5/3/21
#Class: COMP340-001
def evaluate(rootNode):
    #Base case
    if rootNode.lChild == None and rootNode.rChild == None:
        #stop
        return int(rootNode.value)
    #Recursive call
    else:
        result = 0
        leftResult = evaluate(rootNode.lChild)
        rightResult = evaluate(rootNode.rChild)
        if rootNode.type == "PLUS":
            result = leftResult + rightResult
        elif rootNode.type == "MINUS":
            result = leftResult - rightResult
        elif rootNode.type == "MULTIPLICATION":
            result = leftResult * rightResult
        elif rootNode.type == "DIVISION":
            result = leftResult / rightResult
        return result