import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class EntrepotBD{
    
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

    public Article nomArticle(int num) throws SQLException {
        try (Statement st = this.connexion.getConnexion().createStatement();
        ResultSet rs = st.executeQuery("select reference, libelle, prix from ARTICLE where reference = " + num)){
            if (rs.next()) {
                int reference = rs.getInt("reference");
                String libelle = rs.getString("libelle");
                float prix = rs.getFloat("prix");
                Article article = new Article(reference, libelle, prix);
                return article;
            }
        }
        return null;
    }

    public Article PlusGrandNumeroArticleV2()throws SQLException {
        return nomArticle(PlusGrandNumeroArticle());
    }

    public List<Article> listeArticles() throws SQLException {
        List<Article> listeDesArticles = new ArrayList<>();
        try (Statement st = this.connexion.getConnexion().createStatement();
        ResultSet rs = st.executeQuery("select * from ARTICLE")){
            while (rs.next()) {
                int reference = rs.getInt("reference");
                String libelle = rs.getString("libelle");
                float prix = rs.getFloat("prix");
                Article article = new Article(reference, libelle, prix);
                listeDesArticles.add(article);
            }
        }
        return listeDesArticles;
    }

    public void ProcedureEntrepotParDepartement() throws SQLException {
        int cpt = 0;
        String ancienDepartement = null;
        try (Statement st = this.connexion.getConnexion().createStatement();
        ResultSet rs = st.executeQuery("select code, nom, departement from ENTREPOT order by departement")){

            while (rs.next()) {
                int code = rs.getInt("code");
                String nom = rs.getString("nom");
                String departement = rs.getString("departement");

                if (ancienDepartement != null) {
                    if (!ancienDepartement.equals(departement)) {
                        System.out.println("    Dans le " + ancienDepartement + ", il y a " + cpt + " entrepots");
                        cpt = 0;
                    }
                }
                cpt += 1;
                ancienDepartement = departement;
                System.out.println("L'entepot " + code + " de nom " + nom);
            }
            if (ancienDepartement != null) {
        
                System.out.println("Dans le " + ancienDepartement + ", il y a " + cpt + " entrepots");
            }
        }
    }

    public static void main(String[] args) {
        EntrepotBD base = new EntrepotBD();
        try {
            System.out.println("L’article avec le plus grand identifiant est le " + base.PlusGrandNumeroArticle());
            System.out.println("L'article qui a le numéro 1002 est : " + base.nomArticle(1002));
            System.out.println("L’article avec le plus grand identifiant est : " + base.PlusGrandNumeroArticleV2());
            System.out.println("La liste des articles : " + base.listeArticles());
            System.out.println("\n");
            base.ProcedureEntrepotParDepartement();
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }
}
