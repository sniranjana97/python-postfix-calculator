import socket
import sys
import operator

host= '127.0.0.1'; #server host number

stack=[]  #stack for evaluation
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
port= int(sys.argv[1]) #obtain port number
s.bind((host, port))        # Bind to the port
while True:
    s.listen(10000)                 # Client connection
    c, addr = s.accept() #Accept client connection
    while True:
      try:
        equation = c.recv(1024).decode()
        if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()" or not equation:  #Close
            c.send("Quit".encode())
            break
        else:
          print "Server received:" + equation  #Print received equation
        eqn=equation.split(" ")
        while len(eqn) > 0:
          item = eqn.pop(0)
          if item.isdigit():
            stack.append(int(item))

          elif item == "+":
            stack.append(stack.pop() + stack.pop())
            c.send(str(stack.pop()).encode())

          elif item == "-":
            tmp = stack.pop()
            stack.append(stack.pop() - tmp)
            c.send(str(stack.pop()).encode())
          elif item == "*":
            stack.append(stack.pop() * stack.pop())
            c.send(str(stack.pop()).encode())
          elif item == "/":
            tmp = stack.pop()
            if(tmp==0):
              c.send(str("ZeroDiv").encode())
              break;
            else:
              stack.append(stack.pop() / tmp)
            c.send(str(stack.pop()).encode())
          elif item == "^":
            tmp = stack.pop()
            stack.append(pow(stack.pop(), tmp))
            c.send(str(stack.pop()).encode())
          else:
             c.send(str("Invalidchar").encode())#error
             break;

          #result = stack.pop()
      except:
        print "socket recv exception"
        break
