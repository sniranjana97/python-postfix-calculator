import socket
import sys
import operator

host= '127.0.0.1'; #Server host number
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create socket
stack=[]  #stack for evaluation
ostack=[] #stack for operands
result= ""
port= int(sys.argv[1]) #obtain port number
equation=sys.argv[2]

s.connect((host,port))
eqn=equation.split(" ")

while len(eqn) > 0:
  item = eqn.pop(0)

  if item.isdigit():
    stack.append(int(item))

  elif item == "+" or "-" or "*" or "/" or "^":
    x=stack.pop()
    if not stack:
      print "Invalid expression, count of operators is high"
      result= "Ophigh"
      exit()

    y=stack.pop()
    equ=str(y) + " " + str(x) + " " + str(item)
    print "Server sent:" + equ
    s.sendall(equ.encode())
    result = s.recv(1024).decode()
    if result == "Quit":
      print "Closing client connection"
      exit()
    elif result == "ZeroDiv":
      print "You can't divide by 0, try again"
      exit()
    elif result == "Invalidchar":
      print "Invalid character found"
      exit()
    else:
      print "Client received:" + result
    stack.append(int(result))

  else:
    print "Invalid entry"

print "Client received final:" + result

if len(stack) > 1:
  print "Number of integers higher than operators\n Element still on stack is ".join([str(x) for x in stack])
  exit()

s.close();


