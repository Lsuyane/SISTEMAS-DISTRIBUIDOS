from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from datetime import datetime
import socket

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

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
    server = SimpleXMLRPCServer(('0.0.0.0', 8000), requestHandler=RequestHandler, allow_none=True)
    server.register_instance(MensagemServer())

    print("Servidor RPC rodando...")
    server.serve_forever()
