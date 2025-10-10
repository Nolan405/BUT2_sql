import sqlalchemy  
# pour avoir sqlalchemy :
# sudo apt-get update 
# sudo apt-get install python3-sqlalchemy
# pip3 install mysql-connector-python

import getpass  # pour faire la lecture cachée d'un mot de passe

def ouvrir_connexion(user,passwd,host,database):
    """
    ouverture d'une connexion MySQL
    paramètres:
       user     (str) le login MySQL de l'utilsateur
       passwd   (str) le mot de passe MySQL de l'utilisateur
       host     (str) le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
       database (str) le nom de la base de données à utiliser
    résultat: l'objet qui gère le connection MySQL si tout s'est bien passé
    """
    try:
        #creation de l'objet gérant les interactions avec le serveur de BD
        engine=sqlalchemy.create_engine('mysql://'+user+':'+passwd+'@'+host+'/'+database)
        #creation de la connexion
        cnx = engine.connect()
    except Exception as err:
        print(err)
        raise err
    print("connexion réussie")
    return cnx

def plus_grand_numero_article(connexion):
    res = connexion.execute(sqlalchemy.text("SELECT max(reference) FROM ARTICLE"))
    resultat = res.first() 
    return resultat[0]

def nom_article(connexion, num):
    res = connexion.execute(sqlalchemy.text("select reference, libelle, prix from ARTICLE where reference = " + str(num)))
    resultat = res.first() 
    reference = resultat.reference
    libelle = resultat.libelle
    prix = resultat.prix
    return reference, libelle, prix

def PlusGrandNumeroArticleV2(connexion):
    return nom_article(connexion, plus_grand_numero_article(connexion))

def lst_article(connexion):
    lst_article = []
    res = connexion.execute(sqlalchemy.text("select * from ARTICLE"))
    for resultat in res:
        reference = resultat.reference
        libelle = resultat.libelle
        prix = resultat.prix
        dico_un_article = {}
        dico_un_article[reference] = (libelle, prix)
        lst_article.append(dico_un_article)
    return lst_article

def procedure_entrepot_par_departement(connexion):
    print("\n")
    compteur = 0
    ancien_departement = None
    res = connexion.execute(sqlalchemy.text("SELECT code, nom, departement FROM ENTREPOT ORDER BY departement"))
    for resultat in res:  
        code = resultat.code
        nom = resultat.nom
        departement_actuel = resultat.departement
        if ancien_departement is not None:
            if ancien_departement != departement_actuel:
                print(f"    Dans le {ancien_departement}, il y a {compteur} entrepôt(s)")
                compteur = 0
        compteur += 1
        ancien_departement = departement_actuel
        print(f"- {nom} d'id {code}")
    if ancien_departement is not None:
        print(f"    Dans le {ancien_departement}, il y a {compteur} entrepôt(s)\n")

def procedure_lst_entrepot_un_article(connexion, reference):
    res = connexion.execute(sqlalchemy.text(
        "SELECT * FROM ARTICLE NATURAL JOIN STOCKER NATURAL JOIN ENTREPOT " \
        "WHERE reference = " + str(reference)))
    print("Numéro d'article choisie :", reference)
    print("Disponible dans les entrepots :")
    for resultat in res:
        entrepot = resultat.nom
        code_entrepot = resultat.code
        res2 = connexion.execute(sqlalchemy.text("SELECT quantite FROM STOCKER " \
        "WHERE reference = " + str(reference) + " AND code = " + str(code_entrepot)))
        resultat2 = res2.first() 
        quantite = resultat2[0]
        print(f"  - {entrepot} -> {quantite} fois")

def procedure_lst_article_un_entrepot(connexion, code):
    print("\n")
    res = connexion.execute(sqlalchemy.text(
        "SELECT * FROM ARTICLE NATURAL JOIN STOCKER NATURAL JOIN ENTREPOT " \
        "WHERE code = " + str(code)))
    print("Numéro d'entrepot choisi :", code)
    print("Liste d'articles :")
    for resultat in res:
        reference = resultat.reference
        libelle = resultat.libelle
        prix = resultat.prix
        res2 = connexion.execute(sqlalchemy.text("SELECT quantite FROM STOCKER " \
        "WHERE reference = " + str(reference) + " AND code = " + str(code)))
        resultat2 = res2.first() 
        quantite = resultat2[0]
        print(f"  - {libelle} : {prix} -> {quantite} fois")

def val_entrepot(connexion, code):
    print("\n")
    valeur = 0
    res = connexion.execute(sqlalchemy.text(
        "SELECT * FROM ARTICLE NATURAL JOIN STOCKER NATURAL JOIN ENTREPOT " \
        "WHERE code = " + str(code)))
    for resultat in res:
        reference = resultat.reference
        prix = resultat.prix
        res2 = connexion.execute(sqlalchemy.text("SELECT quantite FROM STOCKER " \
        "WHERE reference = " + str(reference) + " AND code = " + str(code)))
        resultat2 = res2.first() 
        quantite = resultat2[0]
        valeur += quantite * prix
    return valeur



if __name__ == "__main__":
    login="morain"
    passwd="morain"
    serveur="servinfo-maria"
    bd="DBmorain"
    cnx=ouvrir_connexion(login,passwd,serveur,bd)
    # ici l'appel des procédures et fonctions
    print("L’article avec le plus grand identifiant est le", plus_grand_numero_article(cnx))
    print("L'article qui a le numéro 1002 est :", nom_article(cnx, 1002))
    print("L’article avec le plus grand identifiant est : ", PlusGrandNumeroArticleV2(cnx))
    print("La liste des articles : ", lst_article(cnx))
    procedure_entrepot_par_departement(cnx)
    procedure_lst_entrepot_un_article(cnx, 1003)
    procedure_lst_article_un_entrepot(cnx, 200)
    print("La valeur de l'entrepot 200 est de : ", val_entrepot(cnx, 200), "€", sep="")
    cnx.close()
