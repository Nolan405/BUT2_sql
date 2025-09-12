insert into TYPES values
    (1, 'ecole'),
    (2, 'mairie'),
    (3, 'association'),
    (4, 'particulier');

insert into OCCUPANT values
    (1, 'ping pong', 'semlknsdvklnfv', 3),
    (2, 'ecole classe 2', 'v<linvsùd', 1),
    (3, 'theatre', 'vrsfvsqrv', 4),
    (4, 'mariage dupond/dubois', 'qrgv<dev<', 2);

insert into SALLE values
    (1, 'salle des fêtes', 80),
    (2, 'salle info', 30),
    (3, 'salle du conseil', 20),
    (4, 'salle des ecureils', 50);

insert into ETREDISPO values
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),

    (2, 1),
    (2, 4),

    (3, 2),

    (4, 1),
    (4, 3);

insert into RESERVER values
    (1, '2025-09-10', 10, 1, 20, 2),
    (1, '2025-09-10', 14, 2, 25, 3),
    (2, '2025-09-11', 9, 2, 15, 2),
    (3, '2025-09-12', 13, 4, 18, 4),
    (4, '2025-09-13', 11, 3, 10, 1);