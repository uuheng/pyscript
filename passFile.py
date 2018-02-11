import socket, os
from time import sleep

def passFile(server_socket):
    fname = input("input file name:")
    save_path = input("input save path:")
    fd = open(fname, 'rb')
    content = fd.read()
    fd.close()
    size = os.path.getsize(fname)
    
    server_socket.sendall(bytes(str(size), encoding="utf8"))
    server_socket.sendall(bytes(save_path, encoding="utf8"))
    sleep(5)
    server_socket.sendall(content)
    res = server_socket.recv(1024)
    print(res)
    return

def main():
    target_host = "192.168.1.106"
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    print("Connect success")
    passFile(client)
    return

if __name__ == '__main__':
    main()
