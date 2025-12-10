#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import func
import time
from datetime import date

from sqlalchemy.orm import registry
mapper_registry = registry()
Base = mapper_registry.generate_base()
# Base class used by my classes (my entities)

from sqlalchemy import select
from sqlalchemy.orm import Session
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

class Personne( Base ):
	__tablename__ = 'PERSONNE'
		
	idp = Column(Integer, primary_key=True)
	nomp = Column(Text)
	prenomp = Column(Text)
	ddnp = Column(Date)
	activites = relationship("Activite", back_populates="animateur")
	lespartp = relationship("Participer", back_populates="participant")
	
	def __init__(self, pk=0, fn="John", ln="Doe", dn=date(2006, 10, 24)):
		self.idp = pk
		self.nomp = fn
		self.prenomp = ln
		self.ddnp = dn
			
	def __str__(self):
		return str(self.idp)+ " " +self.nomp + " " + self.prenomp + " ne le " + str(self.ddnp)

# Definition de la classe Activite (et de la table ACTIVITE)
class Activite( Base ):
    __tablename__ = 'ACTIVITE'

    ida = Column(Integer, primary_key=True)
    noma = Column(Text)
    agemini = Column(Integer)
    annee = Column(Integer)
    nbmaxp = Column(Integer)
    idanim = Column(Integer, ForeignKey("PERSONNE.idp"))
    animateur = relationship("Personne", back_populates="activites")
    lesparta = relationship("Participer", back_populates="lactivite")
    
    def __init__(self, pk=0, na="Détente", am=5, aa=2022, nm=15, ia=0): 
        self.ida = pk
        self.noma = na
        self.agemini = am
        self.annee = aa
        self.nbmaxp = nm
        self.idanim = ia


    def __str__(self):
        res = str(self.ida)+ " " +self.noma + " age mini " + str(self.agemini) 
        res += " en " + str(self.annee) + " nb max participants " 
        res += str(self.nbmaxp) + " animé par " + str(self.idanim)
        return res

class Participer( Base ):
	__tablename__ = 'PARTICIPER'
	
	idp = Column(Integer, ForeignKey("PERSONNE.idp"), primary_key=True)
	#participant = relationship("Personne", backref="Personne.idp")  
	participant = relationship("Personne", back_populates="lespartp")  
	ida = Column(Integer, ForeignKey("ACTIVITE.ida"), primary_key=True) 
	#lactivite = relationship("Activite", backref="Activite.ida")
	lactivite = relationship("Activite",  back_populates="lesparta")
	nbfois = Column(Integer)

	def __init__(self, ip, ia, nbf=0):
		self.idp=ip
		self.ida=ia
		self.nbfois=nbf	
		
	def __str__(self):
		# res = str(self.idp)+ " " + str(self.ida) + " nb fois " + str(self.nbfois) 
		res = str(self.participant)+ " " + str(self.lactivite) + " nb fois " + str(self.nbfois) 
		return res
	def affAct(self):
		return " activite " + str(self.lactivite)
	def affPers(self):
		return " personne " + str(self.participant)	
        
        
        
def activiteTest1(session):    
	a1 = Activite(1, 'Pétanque', 15, 2020, 30, 3) 
	a2 = Activite(2, 'Théatre', 10, 2020, 10, 4)  
	a3 = Activite(3, 'Pétanque', 15, 2022, 30, 3)
	session.add_all([a1, a2, a3])
	session.commit()
	
	print( "--- sélection de toutes les activité ---")
	listeA = session.query(Activite).all()
	for a in listeA: 
		print( a )
		print('animée par ' + str(a.animateur))

def activiteTest2(session): 
	print( "--- sélection de toutes les personnes ---")
	listeA = session.query(Personne).all()
	for p in listeA: 
		print( p )
		for a in p.activites:
			print("     anime : " + str(a))

def modifAnimateur(session):
    # modification de l animateur de l activité 3
    act = session.get(Activite, 3)
    act.idanim = 4
    session.commit()
    
    print( "--- sélection de toutes les personnes ---")
    listeP = session.query(Personne).all()
    for c in listeP: 
        print( c )
        for a in c.activites:
            print("     anime : " + str(a))	

def activite15plus(session):
    # les personnes qui animent une activité à plus de 15 personnes max.
	print( "--- sélection de toutes les personnes qui animent une ")
	print("activité à plus de 15 personnes max.----")
	la15 = session.query(Activite).filter(Activite.nbmaxp>=15).all()
	for a in la15: 
		print(a.animateur)	

def participerTest(session):
	pa1 = Participer(2,2, 10)      
	pa2 = Participer(2,3, 1)      
	pa3 = Participer(2,1, 30)      
	pa4 = Participer(3,2, 10)      
	pa5 = Participer(3,1, 20)      
	session.add_all([pa1, pa2, pa3, pa4, pa5])
	session.commit()

	print( "--- sélection de toutes les participations---")
	listePa = session.query(Participer).all()
	for pa in listePa: 
		print( pa )		

def nombreParticipantsParActivite(session):
	# Il faut ajouter au début : from sqlalchemy import func	
	print( "--- Nombre de personnes par activité ---")
	listeC=session.query(Participer.ida, func.count(Participer.idp)).group_by(Participer.ida).all()
	for elt in listeC: 
		print( elt )

def participantsPetanque(session):
	print( "--- liste des participants à une activité Petanque---")
	listePaPe = session.query(Activite).filter_by(noma="Pétanque").all()
	for pa in listePaPe: 
		print( pa )
		for par in pa.lesparta:
			print("   ", par.affPers())

def personnesActivites(session):
	print( "--- sélection de toutes les personnes et des activité qu'elles font ---")
	listeP = session.query(Personne).all()
	for p in listeP: 
		print( p )
		for pa in p.lespartp:
			print("     ", pa.affAct())    
			
def loaddb(engine, filename):
	'''
		Create all tables and populate them with data in filename
	'''
    
	print( "--- Suppression de toutes les tables de la BD ---" )
	Base.metadata.drop_all(bind=engine)
    
	print( "--- Construction des tables de la BD ---" )
	Base.metadata.create_all(engine)
	session = Session(engine)
    
    
	# importation des données à partir de yaml
	import yaml
	data = yaml.safe_load(open(filename))

	for elt in data:
		if elt['type']=='personne':
			p=Personne(elt['idp'], elt['nomp'], elt['prenomp'], elt['ddnp'])
			session.add(p)
		elif elt['type']=='activite':
			a = Activite(elt['ida'], elt['noma'], elt['agemini'], elt['annee'], elt['nbmaxp'], elt['idanim'])
			session.add(a)
		elif elt['type']=='participer':
			pa = Participer(elt['idp'], elt['ida'], elt['nbfois'])
			session.add(pa)
	# On dit à la DB d'intégrer toutes les nouvelles données:
	session.commit()    
    
def loadbdTest(engine) :
	loaddb(engine, 'dataActivite.yml')  
	session = Session(engine)
    
	print( "--- sélection de toutes les activité ---")
	listeA = session.query(Activite).all()
	for c in listeA: 
		print( c )
		print('animée par ' + str(c.animateur))

	print( "--- sélection de toutes les personnes ---")
	listeP = session.query(Personne).all()
	for p in listeP: 
		print( p )
		for a in p.activites:
			print("     anime : " + str(a))
		for par in p.lespartp:
			print("     participe à :", par.affAct())
			  			
def ormTest(engine):
	print( "--- Suppression de toutes les tables de la BD ---" )
	Base.metadata.drop_all(bind=engine)
	
	print( "--- Construction des tables de la BD (1 table pour l'instant) ---" )
	Base.metadata.create_all(engine)    # Only for the first time
	
	print( "--- Creation de 4 personnes placées dans la BD ---" )
	#Session = sessionmaker(bind=engine)
	#session = Session()
	session = Session(engine)
	
	doe = Personne( 1, "Doe", "John", date(2006, 10, 24))
	session.add( doe )
	alice = Personne(2, "Kolac", "Alice", date(2003, 3, 6))
	james = Personne( 3, "Bond", "James", date(1996, 10, 24))
	jason = Personne( 4, "Bourne", "Jason", date(1999, 12, 24))
	
	session.add_all( [alice, james, jason ] )
	session.commit()
	print( "--- sélection par primary key  idp 3---" )
	#personne = session.query( Personne ).get(3)
	personne = session.get(Personne, 3)
	print( personne )
	
	print( "--- sélection par prenomp commence par Ja---" )
	searchedPersonnes = session.query( Personne ).filter( Personne.prenomp.startswith( "Ja" ) )
	for c in searchedPersonnes: 
		print( c )
	
	print( "--- sélection de toutes les personnes prénommées James ---")
	listeP = session.query(Personne).filter_by( prenomp='James' )
	for c in listeP: 
		print( c )		
	
	print( "--- mise à jour d'une personne spécifique ---")
	personne = session.get( Personne, 1)
	personne.nomp += "!"
	session.commit()        # obligatoire
	
	print( "--- sélection de toutes les personnes ---")
	listeP = session.query(Personne) 
	for c in listeP: 
		print( c )	
		
	print( "--- Suppression d'une personne ---")
	session.delete(personne)
	session.commit()        # obligatoire
	
	print( "--- sélection de toutes les personnes ---")
	listeP = session.query(Personne) 
	for c in listeP: 
		print( c )
	
	activiteTest1(session)
	activiteTest2(session)
	modifAnimateur(session)
	activite15plus(session)
	participerTest(session)
	nombreParticipantsParActivite(session)
	participantsPetanque(session)
	personnesActivites(session)

if __name__ == '__main__':

	# quelle BD va-t-on utiliser?
	#engine = create_engine('sqlite:///animation.db', echo=False) 
	# iut mysql
	engine=create_engine('mysql://chabin:chabin@servinfo-maria/DBchabin')
	#sur machine locale
	#engine=create_engine('mysql://chabin:chabin@localhost/DBchabin')

	#ormTest(engine)
	loadbdTest(engine)
