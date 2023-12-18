import socket
import threading
from datetime import datetime

def handle_client(data, client_address):
    try:
        request = data.decode()
        
        if request == "SolicitarHora":

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            server_socket.sendto(current_time.encode(), client_address)
        else:
            server_socket.sendto("Comando inválido".encode(), client_address)
    except Exception as e:
        print(f"Erro ao processar cliente {client_address}: {e}")

def main():
    host = '127.0.0.1'
    port = 12345

    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"[*] Escutando da {host}:{port}")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"[*] Recebida de {client_address[0]}:{client_address[1]}")

        client_handler = threading.Thread(target=handle_client, args=(data, client_address))
        client_handler.start()

if __name__ == "__main__":
    main()
