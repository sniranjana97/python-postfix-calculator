# python-postfix-calculator
 Four-function Reverse Polish Notation (Postfix) calculator

rpnclient.py:
RUN: python ./rpnclient.py 13002 "4 5 * 4 -"

EXECUTION LOGIC:

INPUT: Obtains two command line argument inputs- port number and the expression.
1. A socket is first created and used to connect to host with s.connect()
2. Input is obtained as string and is split and the client iterates over it.
3. If the input is a digit, it is pushed into a stack (stack[]), else two elements are popped out of stack and sent to the server with the operator as a string. Result is obtained from the server and is pushed into the stack after checking for errors.
4. If the result is a string that says “Quit”, client will close.
5. If the result is a string that says “ZeroDiv”, it would indicate the divide by zero issue.
6. If the result was an “Invalidchar” error, it would mean that the expression had characters such as =, (, % etc.
7. Also, the stack is checked after the first element is popped out. If it was empty, it would indicate that either the previous result was popped out or the expression had only one integer. It would also indicate an overflow of operators. Thus, it would produce an “Ophigh” error.
8. The intermediary and final results are printed at the client side.
9. If the expression contains more integers than the required, it would also cause an error and close the execution.

rpnserver.py:

RUN: python ./rpnserver.py 13002

EXECUTION LOGIC:

INPUT: Obtains a command line argument input- port number
Also obtains a string as input from the client.
1. A socket is created and is bound to a port number using s.bind()
2. The server waits and accepts client connection. It obtains an input expression as string which is split first. If the element is a digit, it is pushed onto stack and if it is an operator, two elements are popped out of stack and evaluated.
3. The resulting integer is then sent to the client.
4. The server helps in checking for errors such as Divide by zero, or invalid character by throwing error statements such as ZeroDiv and Invalidchar.
