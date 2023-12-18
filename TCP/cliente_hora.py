import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    try:
        # Envia a solicitação ao servidor
        request_message = "SolicitarHora"
        client.send(request_message.encode())

        # Recebe e imprime a resposta do servidor
        response = client.recv(1024)
        print(f"[*] Hora do servidor: {response.decode()}")
    finally:
        # Fecha a conexão com o servidor
        client.close()

if __name__ == "__main__":
    main()
