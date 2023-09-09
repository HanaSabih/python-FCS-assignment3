# You work for the MIB (men in black) and would like to decode the messages that they send you.
# The message contains alphabetical characters, white spaces, and Asterix.
# To decode the message, you need a stack.
# You start looping through the message pushing each alphabetical character and white space to your
# stack. Once you reach an Asterix, you pop one character out of your stack.
# Sometimes, you receive an incomplete message. Therefore, if you reach the end of the string and you
# still have characters in your stack, pop all of them out.

# An example of such decoding is:
# Input: SIVLE ****** DAED TNSI ***
# Output: ELVIS ISNT DEAD


##################################################################################
def decode_message(message):
    stack = []
    decoded = []

    for char in message:
        if char.isalpha() or char.isspace():
            stack.append(char)
        elif char == "*":
            if stack:
                stack.pop()

    while stack:
        decoded.append(stack.pop())    
    decoded.reverse()
   
    return "".join(decoded)


