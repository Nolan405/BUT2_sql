select nomO, nomType from OCCUPANT;

select nomS from ETREDISPO natural join SALLE where nomType = 'association';

select distinct nomO from OCCUPANT natural join RESERVER natural join SALLE where nomS = 'salle des fêtes' or nomS = 'salle info';