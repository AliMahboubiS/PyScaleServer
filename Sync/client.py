import sys
import threading
import time
import socket

SOCKET_AMOUNT = 100
HOST = "localhost"
PORT = 9000


def myclient(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.sendall(message)
    result = sock.recv(1024)
    print (result + ' final clnt time {}'.format(time.time()))
    sock.close()

if __name__ == "__main__":
    thread_list = []
    for i in range(SOCKET_AMOUNT):
        msg = "Thread #{}, clnt time {}".format(i, time.time())
        client_thread = threading.Thread(
            target=myclient, args=(HOST, PORT, msg))
        thread_list.append(client_thread)
        client_thread.start()

    waiting = time.time()
    [x.join() for x in thread_list]
    done = time.time()
    print ('DONE {}. Waiting for {} seconds'.format(done, done-waiting))