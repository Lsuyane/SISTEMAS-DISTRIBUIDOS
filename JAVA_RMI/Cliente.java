import java.rmi.Naming;
import java.util.List;

// Classe principal do cliente
public class ClienteMensagens {
    public static void main(String[] args) {
        try {
            // Lookup para obter a referência remota do servidor
            ServicoMensagens servidor = (ServicoMensagens) Naming.lookup("rmi://localhost/ServicoMensagens");

            // Invocação das funções remotas
            servidor.armazenarMensagem("Olá, servidor!");
            servidor.armazenarMensagem("Tudo bem?");
            
            List<String> mensagens = servidor.recuperarMensagens();
            System.out.println("Mensagens no servidor:");
            for (String mensagem : mensagens) {
                System.out.println("- " + mensagem);
            }

            System.out.println("Endereço IP do servidor: " + servidor.obterEnderecoIP());
            System.out.println("Data e Hora do servidor: " + servidor.obterDataEHora());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
