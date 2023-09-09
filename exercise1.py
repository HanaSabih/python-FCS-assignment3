# Use a stack or a queue (or both!) to determine if a given input is a palindrome or not.


################################################################

def palindrome(strg):
    strg = ''.join(strg.split()).lower() 
    stack = []  
    for x in strg:
        stack.append(x)  
    for x in strg:
        if x != stack.pop():
            return False
    return True
