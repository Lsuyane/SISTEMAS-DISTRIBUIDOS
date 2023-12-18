import socket
import threading
from datetime import datetime

def handle_client(client_socket):
    try:
        # Recebe a solicitação do cliente
        request = client_socket.recv(1024).decode()
        if request == "SolicitarHora":
            # Obtém o horário atual
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Envia a resposta ao cliente
            client_socket.send(current_time.encode())
        else:
            client_socket.send("Comando inválido".encode())
    finally:
        # Fecha a conexão com o cliente
        client_socket.close()

def main():
    host = '127.0.0.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Escutando em... {host}:{port}")

    while True:
        client, addr = server.accept()
        print(f"[*] Conexão aceita de {addr[0]}:{addr[1]}")
        # Inicia uma nova thread para lidar com o cliente
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
