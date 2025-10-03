drop table if exists STOCKER;
drop table if exists ENTREPOT;
drop table if exists ARTICLE;

CREATE TABLE ARTICLE (
    reference INT(9),
    libelle VARCHAR(42),
    prix DECIMAL(6,2),
    PRIMARY KEY (reference)
);

CREATE TABLE ENTREPOT (
    code INT(9),
    nom VARCHAR(42),
    departement VARCHAR(42),
    PRIMARY KEY (code)
);

CREATE TABLE STOCKER (
    reference INT(9),
    code INT(9),
    quantite INT(5),
    PRIMARY KEY (reference, code)
);

ALTER TABLE STOCKER
ADD FOREIGN KEY (code) REFERENCES ENTREPOT(code);

ALTER TABLE STOCKER
ADD FOREIGN KEY (reference) REFERENCES ARTICLE(reference);

INSERT INTO ARTICLE (reference, libelle, prix) VALUES
(1001, 'Tournevis', 5.50),
(1002, 'Marteau', 12.90),
(1003, 'Perceuse', 79.99),
(1004, 'Clé à molette', 8.25),
(1005, 'Scie électrique', 129.00);

INSERT INTO ENTREPOT (code, nom, departement) VALUES
(200, 'Entrepôt NordA', 'Nord'),
(201, 'Entrepôt NordB', 'Nord'),
(202, 'Entrepôt Sud', 'Hérault'),
(203, 'Entrepôt Est', 'Bas-Rhin'),
(204, 'Entrepôt OuestA', 'Finistère'),
(205, 'Entrepôt OuestB', 'Finistère'),
(206, 'Entrepôt OuestC', 'Finistère');

INSERT INTO STOCKER (reference, code, quantite) VALUES
(1001, 200, 150),
(1002, 200, 80),
(1003, 201, 40),
(1004, 202, 60),
(1005, 203, 25),
(1001, 203, 10),
(1003, 200, 15);
