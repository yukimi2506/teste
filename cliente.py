import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:2424")

#  Do 10 requests, waiting each time for a response
while True:
    message = input("Insira operacao('soma' 'sub' 'mult')> ")
    socket.send(str, message)
    message = input("valor> ")
    socket.send(int, message)
    message = input("valor> ")
    socket.send(int, message)

    message = socket.recv()
    print("[ %d ]" % message)
