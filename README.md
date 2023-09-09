# python-FCS-assignment3

Stacks and Queues
1. Use a stack or a queue (or both!) to determine if a given input is a palindrome or not.
2. Use a stack or a queue (or both!) to determine if a given expression is balanced.
The expression will contain a combination of these types of parenthesis: (), {}, or []
You have to make sure that for every opening parenthesis, there is a valid closing one.
Ex:
Input: (1+2)-3*[41+6] output: True
Input: (1+2)-3*[41+6} output: False
Input: (1+2)-3*[41+6 output: False
Input: (1+2)-3*]41+6[ output: False
Input: (1+[2-3]*4{41+6}) output: True

Queues
You own a car wash and would like to implement a program to keep up with the queue of cars waiting.
When you open your car wash (at the start of the program), your queue is empty.
Once the cars start coming, you add them to your queue. Every car has a make (string), a color (string)
and a plate number (int).
Once you finish washing a car you remove it from the queue and print all the information about the car.
If no more cars are waiting (the queue is empty), you close your program.

The program contains a menu with the following options:
1. To insert a car to the queue
2. To remove the car from the queue
When you want to add a car to the queue, you should also add the in

Inside class Queue, write the following functions:
 enqueue(c): Insert car cat the rear of the queue.
 dequeue(): Remove and return from the queue the car at the front
 size(): Return the number of cars in the queue.
 isEmpty(): Return a Boolean (True or False) value that indicates whether the queue is empty.
 front(): Return, but do not remove, the front car in the queue

Stack
You work for the MIB (men in black) and would like to decode the messages that they send you.
The message contains alphabetical characters, white spaces, and Asterix.
To decode the message, you need a stack.
You start looping through the message pushing each alphabetical character and white space to your
stack. Once you reach an Asterix, you pop one character out of your stack.
Sometimes, you receive an incomplete message. Therefore, if you reach the end of the string and you
still have characters in your stack, pop all of them out.

An example of such decoding is:
Input: SIVLE ****** DAED TNSI ***
Output: ELVIS ISNT DEAD