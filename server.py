import socket

HOST = '127.0.0.1'
PORT = 65432


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f'* Received: {data}')
                conn.sendall(data.encode('utf-8'))
                data = ''


if __name__ == '__main__':
    main()
