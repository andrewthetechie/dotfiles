import os
import socket

def get_hostname():
    return socket.gethostname()

def main():
    hostname = get_hostname()
    type = input("What is the machine type?")
    print(hostname)
    print(type)

if __name__ == "__main__":
    main()