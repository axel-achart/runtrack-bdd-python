-- Job 03 : Ajouter des valeurs aux tables

INSERT INTO etage(nom, numero, superficie)
    -> VALUES("RDC", "0", "500");

INSERT INTO etage(nom, numero, superficie)
    -> VALUES("R+1", "1", "500");

-------------------------------------------

INSERT INTO salle(nom, id_etage, capacite)
    -> VALUES("Lounge", "1", "100");

INSERT INTO salle(nom, id_etage, capacite)
    -> VALUES("Studio Son", "1", "5");

INSERT INTO salle(nom, id_etage, capacite)
    -> VALUES("Broadcasting", "2", "50");

INSERT INTO salle(nom, id_etage, capacite)
    -> VALUES("Bocal Peda", "2", "4");

INSERT INTO salle(nom, id_etage, capacite)
    -> VALUES("Coworking", "2", "80");

INSERT INTO salle(nom, id_etage, capacite)
    -> VALUES("Studio Video", "2", "5");

-- Dans Git Bash
-- "C:/Program Files/MySQL/MySQL Server 8.0/bin/mysqldump.exe" -u root -p laplateforme > laplateforme.sql
-- Pour exporter