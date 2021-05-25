#Author: Mitchell Noun
#Date: 4/20/21
#Class: COMP340-001
class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

def tokenize(srcCode):
    tokSeq = []
    #blah blah blah
    while srcCode != "":
        char = srcCode[0]
        if char == "+": #Addition token
            newToken = token("PLUS", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "-": #Subtraction token
            newToken = token("MINUS", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "*": #Multiplication token
            newToken = token("MULTIPLICATION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "/": #Division token
            newToken = token("DIVISION", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == "(": #Left parenthesis token
            newToken = token("LPAREN", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == ")": #Right parenthesis token
            newToken = token("RPAREN", char)
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == " ": #Space token
            srcCode = srcCode[1:]
        elif char.isdigit(): #Number token
            numbStr = ""
            while char.isdigit():
                numbStr += char
                srcCode = srcCode[1:]
                if srcCode == "":
                    char = ""
                else:
                    char = srcCode[0]
            #numbStr will have all digits inside it
            newToken = token("NUMBER", numbStr)
            tokSeq.append(newToken)

    return tokSeq