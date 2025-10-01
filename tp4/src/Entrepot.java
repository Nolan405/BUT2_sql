public class Entrepot {
    
    private int code;
    private String nom;
    private String departement;

    public Entrepot(int code, String nom, String departement) {
        this.code = code;
        this.nom = nom;
        this.departement = departement;
    }

    public int getCode() {
        return this.code;
    }

    public String getNom() {
        return this.nom;
    }

    public String getDepartement() {
        return this.departement;
    }

    @Override
    public String toString() {
        return "Entrepot{" +
                "code=" + code +
                ", nom='" + nom + '\'' +
                ", departement='" + departement + '\'' +
                '}';
    }
}
