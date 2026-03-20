import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class EleveBD {
    private Connection co;

    public EleveBD(Connection co) {
        this.co = co;
    }

    public int getNBMatiere(String domaine) throws SQLException {
        try (PreparedStatement  st = this.co.getConnexion().prepareStatement();
        ResultSet rs = st.executeQuery("select reference, libelle, prix from ARTICLE where reference = ?")) {
            st.setString(1, domaine);

                if (rs.next()) {
                    nb = rs.getInt(1); // récupérer le COUNT(*)
                }
        }
    }
}