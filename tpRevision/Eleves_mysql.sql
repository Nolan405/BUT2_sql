-- CREATE DATABASE IF NOT EXISTS ELEVES DEFAULT CHARACTER SET UTF8MB4 COLLATE utf8_general_ci;
-- USE ELEVES;

CREATE TABLE ELEVE (
  num INT(9),
  nom VARCHAR(42),
  prenom VARCHAR(42),
  bac VARCHAR(42),
  annee INT(4)
);

CREATE TABLE MATIERE (
  reference INT(9),
  nom VARCHAR(42),
  domaine VARCHAR(42),
  nbheurestotale INT(2)
);

CREATE TABLE SUIVRE (
  num INT(9),
  reference INT(9),
  nbheureseffectuees INT(2)
);

CREATE TABLE ANCIEN (
  num INT(9),
  nom VARCHAR(42),
  prenom VARCHAR(42),
  bac VARCHAR(42),
  annee INT(4)
);

