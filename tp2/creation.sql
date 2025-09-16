-- CREATE DATABASE IF NOT EXISTS ENTREPOT DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
-- USE ENTREPOT;

drop table if exists STOCKER;
drop table if exists ARTICLE;
drop table if exists ENTREPOT;

CREATE TABLE ARTICLE (
  reference INT(9),
  libelle VARCHAR(42),
  prix DECIMAL(6,2),
  PRIMARY KEY (reference)
) ;

CREATE TABLE ENTREPOT (
  code INT(9),
  nom VARCHAR(42),
  departement VARCHAR(42),
  PRIMARY KEY (code)
) ;

CREATE TABLE STOCKER (
  reference INT(9),
  code INT(9),
  quantite INT(5),
  PRIMARY KEY (reference, code)
) ;


ALTER TABLE STOCKER ADD FOREIGN KEY (code) REFERENCES ENTREPOT (code);
ALTER TABLE STOCKER ADD FOREIGN KEY (reference) REFERENCES ARTICLE (reference);