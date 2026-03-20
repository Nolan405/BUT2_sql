-- question 1

-- clefs primaires  : en MAJUSCULE
-- clefs étrangères : #

-- ELEVE [NUM, nom, prenom, bac, annee]
-- MATIERE [REFERENCE, nom, domaine, nbHeuresTotales]
-- SUIVRE [#NUM, #REFERENCES, nbHeuresEfffectuees]

-- dépendances fonctionnelles :
-- num -> nom, prenom, bac, annee
-- reference -> nom, domaine, nbHeuresTotale
-- num, references -> nbHeuresEffectuees
-- domaine, nom -> reference

-- question 2

delimiter |
create or replace function getNbElevesObtenuBac(bacDemmande varchar(50)) returns int
begin
    declare nbEleves int default 0;

    select count(*) into nbEleves from ELEVE where bac = bacDemmande;

    return nbEleves;
end |
delimiter ;

select getNbElevesObtenuBac("S");

-- question 3

delimiter |
create or replace function getNbTotalHeuresUnEleve(numEleve int) returns int
begin 
    declare nbTotalHeures int default 0;

    select sum(nbHeuresEffectuees) into nbTotalHeures from ELEVE
    natural join SUIVRE where num = numEleve;

    return nbTotalHeures;
end |
delimiter ;

select getNbTotalHeuresUnEleve(1);

-- question 4

delimiter |
create or replace procedure AllMatiereSuivie(numDemmande int)
begin
    declare res varchar(500) default "";
    declare fini boolean default false;
    declare p_num int;
    declare p_prenom varchar(50);
    declare p_nom varchar(50);
    declare p_nom_matiere varchar(50);

    declare cur_matiere cursor for 
        select E.num, E.nom, prenom, M.nom from ELEVE as E, SUIVRE as S, MATIERE as M 
        where E.num = S.num and M.reference = S.reference and E.num = numDemmande;
    
    declare continue handler for not found set fini = true;

    open cur_matiere;

    while not fini do

        fetch cur_matiere into p_num, p_nom, p_prenom, p_nom_matiere;

        if not fini then 
            set res = concat(res, "\n - La matière ", p_nom_matiere);
        end if;

    end while;
    close cur_matiere;
    select res;
end |
delimiter ; 

call AllMatiereSuivie(1);

-- question 5

delimiter |
create or replace trigger UneMatiereMemeNomDansDomaine before insert on MATIERE for each row
begin
    declare nb int;

    select count(*) into nb from MATIERE where nom = NEW.nom;

    if nb > 0 then
    SIGNAL SQLSTATE"45000"
        set MESSAGE_TEXT = "Vous ne pouvez paqs mettre le même nom d'une matière deux fois dans un même domaine";
    end if;
end |
delimiter ;