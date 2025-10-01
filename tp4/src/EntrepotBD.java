import java.sql.*;

public class EntrepotBD {
    
    private ConnexionMySQL connexion;

    public EntrepotBD(){
        this.connexion = new ConnexionMySQL(
            "servinfo-maria", "DBmorain", "morain", "morain");
    }

    public int PlusGrandNumeroArticle()throws SQLException {
        int maxRef = 0;
        try (Statement st = this.connexion.getConnexion().createStatement();
        ResultSet rs = st.executeQuery("select max(reference) from ARTICLE")){
            if (rs.next()) {
                maxRef = rs.getInt(1);
            }
        }
        return maxRef;
    }

    public static void main(String[] args) {
        EntrepotBD base = new EntrepotBD();
        try {
            System.out.println("L’article avec le plus grand identifiant est le " + base.PlusGrandNumeroArticle());
        } catch (SQLException e) {
            e.getMessage();
        }
    }
}
