from xmlrpc.client import ServerProxy

def main():
    server = ServerProxy("http://hostnamedoservidor:8000/RPC2")

    mensagem = "Olá, servidor RPC!"
    resultado_armazenamento = server.armazenar_mensagem(mensagem)
    print(resultado_armazenamento)

    lista_mensagens = server.obter_lista_mensagens()
    print("Lista de Mensagens:", lista_mensagens)

    ip_servidor = server.obter_ip_servidor()
    print("IP do Servidor:", ip_servidor)

    data_hora_servidor = server.obter_data_hora_servidor()
    print("Data e Hora do Servidor:", data_hora_servidor)

if __name__ == "__main__":
    main()
