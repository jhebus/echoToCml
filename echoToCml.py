from socket import *
import sys

#HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
#PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def echo_to_cml(port):
    print('Listening on port %d' % (port))
    in_sock = socket(AF_INET, SOCK_STREAM)
    in_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    in_sock.bind(('', port))
    #in_sock.bind(('', PORT))
    in_sock.listen(5)

    while True:
        conn, addr = in_sock.accept()
        print('Accept', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print data

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'Usage python echo_to_cml.py <port number to listen>'
    else:
        echo_to_cml(int(sys.argv[1]))
