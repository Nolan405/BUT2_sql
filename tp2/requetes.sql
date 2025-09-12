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

/*3*/
delimiter |
create or replace function maxRefArticle() returns int
begin
    declare res int;
    select ifnull(max(reference), 0) into res from ARTICLE;
    return res;
end |
delimiter ;

select maxRefArticle();
