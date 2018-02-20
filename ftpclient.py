import ftplib
import sys

if len(sys.argv) < 2:
    tmp = input("please input server address:")
    sys.argv.append(tmp)
server_address = sys.argv[1]
ftp = ftplib.FTP(server_address)
print(ftp.getwelcome())
ftp.login('uh3ng', '111111xzh')

def upload(fname):
    fd = open(fname, 'rb')
    new_name = input("input new name:")
    ftp.storbinary("STOR %s" % new_name, fd)
    fd.close()
    print("upload finished")
	
def download(fname):
    new_path = "i:\\pyscript\\download\\" + fname
    fd = open(new_path, 'wb')
    ftp.retrbinary("RETR %s" % fname, fd.write)
    fd.close()
    print("download finished")

def main():
    op = input("what do you want?(u/d/q)")
    if op == "u":
        fname = input("input the file of path:")
        upload(fname)
    elif op == "d":
        fname = input("input the file name:")
        download(fname)
    else:
        print("quit now!")
        ftp.quit()
        sys.exit(0)
    ftp.quit()

if __name__ == '__main__':
    main()