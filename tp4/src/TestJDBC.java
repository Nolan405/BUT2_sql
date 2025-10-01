
public class TestJDBC {
    
    private ConnexionMySQL connexion;

    public TestJDBC(){
        this.connexion = new ConnexionMySQL(
            "servinfo-maria", "DBmorain", "morain", "morain");
    }

    public ConnexionMySQL getConnexion() {
        return connexion;
    }

    public static void main(String[] args) {
        TestJDBC test = new TestJDBC();
        System.out.println("Connexion établie : " + test.getConnexion().getConnecte());
    }
}