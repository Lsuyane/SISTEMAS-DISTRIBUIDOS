import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Conversao extends Remote {
    double convertEuroToReal(double euroAmount) throws RemoteException;
    double convertRealToEuro(double realAmount) throws RemoteException;
    double convertDollarToReal(double dollarAmount) throws RemoteException;
    double convertRealToDollar(double realAmount) throws RemoteException;
}
