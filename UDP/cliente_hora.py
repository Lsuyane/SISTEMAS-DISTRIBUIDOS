import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        request_message = "SolicitarHora"
        client_socket.sendto(request_message.encode(), (host, port))

        response, _ = client_socket.recvfrom(1024)
        print(f"[*] Hora do servidor: {response.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
