from xmlrpc.client import ServerProxy

def local_server_example():
    server = ServerProxy('http://localhost:8000')
    print("Data e Hora Atual (Local):", server.get_current_datetime())
    print("Quantidade de Chamadas Recebidas (Local):", server.get_call_count())

def remote_server_example():
    server = ServerProxy('http://<ip_do_servidor>:8000')  
    print("Data e Hora Atual (Remoto):", server.get_current_datetime())
    print("Quantidade de Chamadas Recebidas (Remoto):", server.get_call_count())

if __name__ == "__main__":
    print("Exemplo de chamadas para o servidor local:")
    local_server_example()

    print("\nExemplo de chamadas para um servidor remoto:")
    remote_server_example()
