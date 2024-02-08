import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class Servidor extends UnicastRemoteObject implements Conversao {
    protected Servidor() throws RemoteException {
        super();
    }

    @Override
    public double convertEuroToReal(double euroAmount) throws RemoteException {
        // Simplesmente retornando o dobro para fins de exemplo
        return euroAmount * 2;
    }

    @Override
    public double convertRealToEuro(double realAmount) throws RemoteException {
        // Simplesmente retornando a metade para fins de exemplo
        return realAmount / 2;
    }

    @Override
    public double convertDollarToReal(double dollarAmount) throws RemoteException {
        // Simplesmente retornando o dobro para fins de exemplo
        return dollarAmount * 2;
    }

    @Override
    public double convertRealToDollar(double realAmount) throws RemoteException {
        // Simplesmente retornando a metade para fins de exemplo
        return realAmount / 2;
    }

    public static void main(String[] args) {
        try {
            Servidor server = new Servidor();
            java.rmi.registry.LocateRegistry.createRegistry(1099);
            java.rmi.Naming.rebind("CurrencyConverterService", server);
            System.out.println("Servidor pronto para conversão de moedas...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
