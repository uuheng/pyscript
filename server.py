import socket, threading
import os
from time import sleep

def main():
    bind_ip = '127.0.0.1'
    bind_port = 9999

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((bind_ip, bind_port))

    server.listen(5)
    print("[*] Listening on %s:%d" % (bind_ip, bind_port))

    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        op = client.recv(1024)
        if op == b'0':
            getData(client)
        else:
            getFile(client)
        #print(client.recv(2048))

def getFile(client_socket):
    print("In getFile... ")
    size = int(client_socket.recv(1024))
    print(size)
    path = client_socket.recv(1024)
    print(path)
    buffer = b''
    data = b''
    tmp = 0
    while tmp < size:
        print("ready recv ... " + str(tmp))
        data = client_socket.recv(4096)
        #print(b"This is data: " + data)
        tmp += len(data)
        buffer += data
    with open(path, 'wb') as fd:
        fd.write(buffer)
    client_socket.sendall(b'success')
    print("recv success")
    client_socket.close()

def getData(client_socket):
    #sleep(4)
    print("In getdata ...")
    buffer = b''
    #data = b''
    while True:
        print("Ready recv")
        buffer = client_socket.recv(2048)
        print(b'This is buffer: ' + buffer)
        if b'quit' == buffer:
            break
        #buffer += data
        print(buffer)
        msg = run_cmd(buffer)
        client_socket.sendall(msg)
        #client_socket.sendall(b"ok")
    client_socket.close()
    print('next ... ')

def run_cmd(cmd):
    fd = os.popen(cmd.decode())
    msg = fd.read()
    fd.close()
    return bytes(msg, encoding="gbk")

if __name__ == '__main__':
    main()

    

#def handle_client(client_socket):
#    request = client_socket.recv(1024)
#    print("[*] Received: %s" % request)
#    client_socket.send(bytes("ACK!", encoding="utf8"))
#    client_socket.close()

#while True:
#    client, addr = server.accept()
#    print ("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))

#    client_handler = threading.Thread(target=handle_client, args=(client,))
#    client_handler.start()