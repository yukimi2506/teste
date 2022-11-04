import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:2424")

op = []

while True:
    #  Wait for next request from client
    message = socket.recv()
    op.append(message)
    time.sleep(1)

    if op[2]:
        if op[0] == 'soma':
            soma = op[1] + op[2]
            socket.send(soma)
            for pos in range(3):
                del op[pos]

        if op[0] == 'sub':
            sub = op[1] + op[2]
            socket.send(sub)
            for pos in range(3):
                del op[pos]

        if op[0] == 'mult':
            m = op[1] + op[2]
            socket.send(m)
            for pos in range(3):
                del op[pos]