from socket import *
from json import loads
from math import sin

with socket(AF_INET, SOCK_STREAM) as server_:
    print('Server is on')
    server_.bind(('127.0.0.1', 8181))
    server_.listen()
    _socket, _address = server_.accept()
    
    print(f'get socket from {_address}')

    with _socket:
        while True:
            get_data = _socket.recv(1024)
            if not get_data:
                break
            
            loaded = loads(get_data.decode())
            
            first = loaded['first']
            second = loaded['second']
            third = loaded['third']

            result = first*second/third
            message = "data: " + str(first) + ", " + str(second) + ", " + str(third) + "\n (x+y)*z = " + str(result)
            print(message)
            _socket.sendall(message.encode())
