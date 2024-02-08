import java.rmi.Naming;

public class Cliente {
    public static void main(String[] args) {
        try {
            Conversao currencyConverter = (Conversao) Naming.lookup("rmi://localhost:1099/CurrencyConverterService");

            double euroAmount = 100;
            double realAmount = 200;

            System.out.println("Conversão de Euro para Real: " + currencyConverter.convertEuroToReal(euroAmount));
            System.out.println("Conversão de Real para Euro: " + currencyConverter.convertRealToEuro(realAmount));

            double dollarAmount = 50;

            System.out.println("Conversão de Dólar para Real: " + currencyConverter.convertDollarToReal(dollarAmount));
            System.out.println("Conversão de Real para Dólar: " + currencyConverter.convertRealToDollar(realAmount));

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
