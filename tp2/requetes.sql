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
declare res varchar(500) default '';
    declare fini int default FALSE;
    declare p_code int;
    declare p_nom varchar(50);
    declare p_departement varchar(50);

    declare cur_entrepots cursor for 
        select code, nom, departement 
        from ENTREPOT 
        order by code;
    
    declare continue handler for not found set fini = TRUE;

    open cur_entrepots;
    while not fini do
        fetch cur_entrepots into p_code, p_nom, p_departement;

        if not fini then
            set res = concat(res, p_code, ' ', p_nom, ' ', p_departement, '  ');
        end if;
    end while;
    close cur_entrepots;
    select res;
end |
delimiter ;

call tousLesEntrepots();

/*5*/
delimiter |
create or replace procedure tousLesEntrepotsTriés()
begin
declare res varchar(500) default '';
    declare fini int default FALSE;
    declare p_code int;
    declare p_nom varchar(50);
    declare p_departement varchar(50);
    declare p_departement_prec varchar(50) default '';
    declare p_compteur_dept int default 0;

    declare cur_entrepots_triés cursor for 
        select code, nom, departement
        from ENTREPOT 
        order by departement;
    
    declare continue handler for not found set fini = TRUE;

    open cur_entrepots_triés;
    while not fini do
        fetch cur_entrepots_triés into p_code, p_nom, p_departement;
        
        if not fini then

            if p_departement_prec != p_departement THEN

                IF p_departement_prec != '' THEN
                    select CONCAT('Dans le  ', p_departement_prec, ', il y a ', p_compteur_dept, ' entrepots');
                end if;

                set p_compteur_dept = 0;
                set p_departement_prec = p_departement;

            end if;

            set p_compteur_dept = p_compteur_dept + 1;
            
            set res = concat(res, p_code, ' ', p_nom, ' ', p_departement, ' ');
        end if;
    end while;
    close cur_entrepots_triés;
    IF p_departement_prec != '' THEN
        SELECT CONCAT('Dans le ', p_departement_prec, ', il y a ', p_compteur_dept, ' entrepôts');
    END IF;
    select res;
end |
delimiter ;

call tousLesEntrepotsTriés();