import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

interface ServicoMensagens extends Remote {
    void armazenarMensagem(String mensagem) throws RemoteException;
    List<String> recuperarMensagens() throws RemoteException;
    String obterEnderecoIP() throws RemoteException;
    String obterDataEHora() throws RemoteException;
}

class ServidorMensagensImpl extends UnicastRemoteObject implements ServicoMensagens {
    private List<String> listaMensagens;

    public ServidorMensagensImpl() throws RemoteException {
        super();
        this.listaMensagens = new ArrayList<>();
    }

    @Override
    public void armazenarMensagem(String mensagem) throws RemoteException {
        listaMensagens.add(mensagem);
        System.out.println("Mensagem armazenada: " + mensagem);
    }

    @Override
    public List<String> recuperarMensagens() throws RemoteException {
        return new ArrayList<>(listaMensagens);
    }

    @Override
    public String obterEnderecoIP() throws RemoteException {
        return "127.0.0.1";
    }

    @Override
    public String obterDataEHora() throws RemoteException {
        SimpleDateFormat formatoDataHora = new SimpleDateFormat("yyyy-MM-dd HH:mm");
        return formatoDataHora.format(new Date());
    }
}

// Classe principal do servidor
public class ServidorMensagens {
    public static void main(String[] args) {
        try {
            ServicoMensagens servidor = new ServidorMensagensImpl();

            java.rmi.registry.LocateRegistry.createRegistry(1099);
            java.rmi.Naming.rebind("ServicoMensagens", servidor);

            System.out.println("Servidor pronto para receber chamadas remotas...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}