-- Job 02 : Créer 2 tables dans la base de donnée LaPlateforme

CREATE TABLE etage(id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255), numero INT, superficie INT);

CREATE TABLE salle(id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255), id_etage INT, capacite INT);

SHOW TABLES;