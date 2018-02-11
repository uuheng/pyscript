import socket
from time import sleep

def getFile(client_socket):
    print("Ready get file...")
    size = int(client_socket.recv(1024))
    print("File size is %d" % size)
    path = client_socket.recv(1024)
    print("File will save at %s" % path)
    file_buffer = b''
    data = b''
    length = 0
    while length < size:
        data = client_socket.recv(4096)
        length += len(data)
        file_buffer += data
    with open(path, 'wb') as fd:
        fd.write(file_buffer)
    client_socket.sendall(b'Get success')
    print("Recv finished")
    client_socket.close()
    return

def main():
    bind_ip = '192.168.1.106'
    bind_port = 9999
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print("Listening on %s:%d" % (bind_ip, bind_port))
    while True:
        client, addr = server.accept()
        print("Accept connection from: %s:%d" % (addr[0], addr[1]))
        getFile(client)
    return

if __name__ == '__main__':
    main()
