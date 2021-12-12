from socket import *
from json import dumps

with socket(AF_INET, SOCK_STREAM) as client_:

    client_.connect(('127.0.0.1', 8181))
    first = int(input('first num = '))
    second = int(input('second num = '))
    third = int(input('third num = '))
    
    data = {'first': first, 'second': second, 'third': third}

    client_.sendall(dumps(data).encode())
    print(client_.recv(1024))
