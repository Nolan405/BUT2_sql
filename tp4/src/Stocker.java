public class Stocker {
    
    private int reference;
    private String nom;
    private String departement;

    public Stocker(int reference, String nom, String departement) {
        this.reference = reference;
        this.nom = nom;
        this.departement = departement;
    }

    public int getReference() {
        return this.reference;
    }

    public String getNom() {
        return this.nom;
    }

    public String getDepartement() {
        return this.departement;
    }

    @Override
    public String toString() {
        return "Stocker{" +
                "reference=" + reference +
                ", nom='" + nom + '\'' +
                ", departement='" + departement + '\'' +
                '}';
    }
}
