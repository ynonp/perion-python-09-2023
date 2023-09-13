import socket as sock
import itertools


def open_ports():
    for port in range(1, 65_536):
        create_socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        destination = ("127.0.0.1", port)
        result = create_socket.connect_ex(destination)
        if result == 0:
           yield port
        create_socket.close()

print(list(itertools.islice(open_ports(), 2)))
