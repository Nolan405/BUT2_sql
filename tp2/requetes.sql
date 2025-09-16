/*exercice n°1*/

/*1*/
prepare articleMoins from "select * from ARTICLE where prix > ?";
execute articleMoins using 20;

set @dix = 100;  /*créer une variable*/
execute articleMoins using @dix;
desallocable prepare articleMoins   /*supprime*/

/*2*/
set @libelle = "Chaise";
set @departement = "Cher";
prepare quantiteStock from "select quantite, libelle, departement from STOCKER
natural join ARTICLE natural join ENTREPOT where libelle = ? and departement = ?";
execute quantiteStock using @libelle, @departement;

/*exercice n°2*/

/*1*/
delimiter |
create or replace function maxRefArticle() returns int
begin
    declare res int;
    select ifnull(max(reference), 0) into res from ARTICLE;
    return res;
end |
delimiter ;

select maxRefArticle();

/*2*/
delimiter |
create or replace function deptEntrepot(codeEntrepot int) returns varchar(255)
begin
    declare res varchar(255);
    select departement into res from ENTREPOT where code = codeEntrepot;
    return res;
end |
delimiter ;

select deptEntrepot(2);

/*3*/
delimiter |
create or replace function valEntrepot(codeEntrepot int) returns int
begin
    declare res int;
    select sum(prix*quantite) into res from ARTICLE 
    natural join STOCKER natural join ENTREPOT
    where code = codeEntrepot;
    return res;
end |
delimiter ;

select valEntrepot(2);

/*4*/
delimiter |
create or replace procedure tousLesEntrepots()
begin
    select * from ENTREPOT;
end |
delimiter ;

call tousLesEntrepots();

/*5*/
delimiter |
create or replace procedure tousLesEntrepotsTries()
begin
    select departement, nom from ENTREPOT order by departement;

    select departement, count(*) as nbEntrepots from ENTREPOT 
    group by departement order by departement;
end |
delimiter ;

call tousLesEntrepotsTries()


/*6*/
create or replace procedure tousLesEntrepotsTries_valeur()
begin
    declare departement varchar(50);
    declare nom varchar(50);
    
    call tousLesEntrepotsTries();

    select departement, nom;
end |
delimiter ;

call tousLesEntrepotsTries_valeur()
