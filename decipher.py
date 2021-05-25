#Author: Mitchell Noun
#Date: 5/5/21
#Class: COMP340-001
def decipher(babyExp):
    srcCode = ""
    
    ##Main part##
    #Replaces babyExp string characters with interpreted string characters
    srcCode = babyExp.replace("pee", "+")
    srcCode = srcCode.replace("gah", "-")
    srcCode = srcCode.replace("milk", "*")
    srcCode = srcCode.replace("heh", "/")
    srcCode = srcCode.replace("mama", "(")
    srcCode = srcCode.replace("dada", ")")
    srcCode = srcCode.replace("baaaaaaaaa", "9")
    srcCode = srcCode.replace("baaaaaaaa", "8")
    srcCode = srcCode.replace("baaaaaaa", "7")
    srcCode = srcCode.replace("baaaaaa", "6")
    srcCode = srcCode.replace("baaaaa", "5")
    srcCode = srcCode.replace("baaaa", "4")
    srcCode = srcCode.replace("baaa", "3")
    srcCode = srcCode.replace("baa", "2")
    srcCode = srcCode.replace("ba", "1")
    srcCode = srcCode.replace("b", "0")
    srcCode = srcCode.replace(" ", "")
    #Returns interpreted string
    return srcCode