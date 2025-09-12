drop table if exists RESERVER;
drop table if exists ETREDISPO;
drop table if exists OCCUPANT;
drop table if exists TYPES;
drop table if exists SALLE;

create table TYPES(
    idType int primary key,
    nomType varchar(50)
);

create table OCCUPANT(
    idO int primary key,
    nomO varchar(50),
    caracteristique varchar(50),
    idType int
);

create table SALLE(
    idS int primary key,
    nomS varchar(50),
    capacite varchar(50)
);

create table ETREDISPO(
    idS int,
    idType int,
    primary key(idS, idType)
);

create table RESERVER(
    idS int,
    journee varchar(50),
    heure int,
    idO int,
    nbPersonnes int,
    durree int,
    check (heure > 0),
    check (durree > 0),
    check (heure + durree <= 24),
    primary key(idS, journee, heure)
);

alter table OCCUPANT add constraint fk_idType1 foreign key (idType) references TYPES(idType);
alter table ETREDISPO add constraint fk_idType2 foreign key (idType) references TYPES(idType);
alter table ETREDISPO add constraint fk_idS1 foreign key (idS) references SALLE(idS);
alter table RESERVER add constraint fk_idS2 foreign key (idS) references SALLE(idS);
alter table RESERVER add constraint fk_idO foreign key (idO) references OCCUPANT(idO);