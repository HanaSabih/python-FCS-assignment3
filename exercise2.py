# Use a stack or a queue (or both!) to determine if a given expression is balanced.
# The expression will contain a combination of these types of parenthesis: (), {}, or []
# You have to make sure that for every opening parenthesis, there is a valid closing one.
# Ex:
# Input: (1+2)-3*[41+6] output: True
# Input: (1+2)-3*[41+6} output: False
# Input: (1+2)-3*[41+6 output: False
# Input: (1+2)-3*]41+6[ output: False
# Input: (1+[2-3]*4{41+6}) output: True


#############################################################################################


def is_balanced(strg):
    stack = []
    opn = "([{"
    cl = ")]}"
    bracket = {')': '(', '}': '{', ']': '['}

    for x in strg:
        if x in opn:
            stack.append(x)
        elif x in cl:
            if not stack or stack.pop() != bracket[x]:
                return False

    return not stack 

