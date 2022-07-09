import socket

HOST = '127.0.0.1'
PORT = 65432


# implements the client:
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send("Thank you for connecting me".encode('utf-8'))
        while True:
            data = s.recv(1024).decode('utf-8')
            if not data:
                break
            print(f'\n-> Server sent: {data}')

            data = input('> ')
            if not data:
                break
            s.sendall(data.encode('utf-8'))


if __name__ == '__main__':
    main()
