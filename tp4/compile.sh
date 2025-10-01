echo "Compilation en cours..."
javac -d bin src/*.java
if [ $? -ne 0 ]; then
    echo "❌ Erreur de compilation"
    exit 1
fi
echo "✓ Compilation réussie"

echo "Lancement de l'application..."
java -cp bin:/usr/share/java/mariadb-java-client.jar EntrepotBD
