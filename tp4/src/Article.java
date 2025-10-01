public class Article {
    
    private int reference;
    private String libelle;
    private float prix;

    public Article(int reference, String libelle, float prix) {
        this.reference = reference;
        this.libelle = libelle;
        this.prix = prix;
    }

    public int getReference() {
        return this.reference;
    }

    public String getLibelle() {
        return this.libelle;
    }

    public float getPrix() {
        return this.prix;
    }

    @Override
    public String toString() {
        return "Article{" +
                "reference=" + reference +
                ", libelle='" + libelle + '\'' +
                ", prix=" + prix +
                '}';
    }
}
