import sys
from socket import *


def validate_input_lengths():
    EXPECTED_LEN = 3
    if len(sys.argv) != EXPECTED_LEN:
        print("usage: twist.py", end=" ")
        print("[DNS_name] [filename]")
        print(" " * 16 + "[IP_address] [filename]")
        sys.exit()


def make_socket_and_connect():
    sock = socket(AF_INET, SOCK_STREAM)
    hostname = sys.argv[1]
    addr = (hostname, 80)
    sock.connect(addr)
    return sock


def curl(sock):
    filename = sys.argv[2]
    msg1 = "GET " + filename + " HTTP/1.1\n"
    sock.sendall(msg1.encode())
    hostname = sys.argv[1]
    msg2 = "Host: " + hostname + "\n"
    sock.sendall(msg2.encode())
    msg3 = "\n"
    sock.sendall(msg3.encode())
    sock.shutdown(SHUT_WR)

    curr_stream = sock.recv(1024).decode()
    data = curr_stream
    while len(curr_stream) != 0:
        curr_stream = sock.recv(1024).decode()
        data += curr_stream
    print(data)


def main():
    validate_input_lengths()
    sock = make_socket_and_connect()
    curl(sock)


main()
