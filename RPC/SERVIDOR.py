from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime

class RPCServer:
    def __init__(self):
        self.call_count = 0

    def get_current_datetime(self):
        self.call_count += 1
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_call_count(self):
        return self.call_count

def run_server():
    server = SimpleXMLRPCServer(('localhost', 8000), logRequests=True)
    server.register_instance(RPCServer())
    print("Servidor RPC iniciado. Aguardando chamadas...")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
