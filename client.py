import socket, sys, os
from time import sleep
def main():
    target_host = "192.168.1.100"
    target_port = 9999
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, target_port))
    print("Connect Success!")
    sleep(2)
    op = input("1 for file, 0 for shell")
    if op == '0':
        client.send(b'0')
        uploadData(client)
    elif op == '1':    
        client.send(b'1')
        uploadFile(client)
    else:
        print("input 1 or 0")
    #client.close()

def uploadData(s):
    content = ''
    while content != 'quit':
        content = input('>')
        #content = "asdfasdfasdf"
        #sleep(2)
        s.sendall(bytes(content, encoding="utf8"))
        #s.sendall(b'byebye')
        response = s.recv(4096)
        print(response.decode('gbk'))

def uploadFile(s):
    fname = input("input file name: ")
    store_path = input("store path: ")
    fd = open(fname, 'rb')
    content = fd.read()
    fd.close()
    #sleep(2)
    #print(content)
    size = os.path.getsize(fname)
    s.sendall(bytes(str(size), encoding="utf8"))
    s.sendall(bytes(store_path, encoding="utf8"))
    sleep(1)
    s.sendall(content)
    #s.sendall(b'byebye')
    response = s.recv(1024)
    print(response)

if __name__ == "__main__":
    main()