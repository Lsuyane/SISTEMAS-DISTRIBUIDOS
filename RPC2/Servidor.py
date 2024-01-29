from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
import socket

class MensagemServer:
    def __init__(self):
        self.mensagens = []

    def armazenar_mensagem(self, mensagem):
        self.mensagens.append(mensagem)
        return "Mensagem armazenada com sucesso."

    def obter_lista_mensagens(self):
        return self.mensagens

    def obter_ip_servidor(self):
        return socket.gethostbyname(socket.gethostname())

    def obter_data_hora_servidor(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M")

if __name__ == "__main__":
    server = SimpleXMLRPCServer(('localhost', 8000), allow_none=True)
    server.register_instance(MensagemServer())

    print("Servidor RPC rodando...")
    server.serve_forever()
