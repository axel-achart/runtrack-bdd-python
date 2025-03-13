# Job 08 : Zoo, animaux et cages (SQL et Python)

# Création de la database et des tables et de leurs contenus via MySQL
"""CREATE DATABASE zoo;

USE zoo;

CREATE TABLE animal(id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(25), race VARCHAR(25), id_type_cage INT, date_naissance VARCHAR(10), pays_origine VARCHAR(25));
CREATE TABLE cage(id INT PRIMARY KEY AUTO_INCREMENT, capacite INT, superficie INT, capacite_max INT);


INSERT INTO animal(nom, race, id_type_cage, date_naissance, pays_origine)
    -> VALUES("Dauphin", "Cetace", 1, "28-04-2006", "Vietnam");
INSERT INTO animal(nom, race, id_type_cage, date_naissance, pays_origine)
    -> VALUES("Baleine", "Cétacé", 1, "13-02-2007", "Vietnam");
INSERT INTO animal(nom, race, id_type_cage, date_naissance, pays_origine)
    -> VALUES("Chien", "Mammifere", 2, "23-09-2005", "France");
INSERT INTO animal(nom, race, id_type_cage, date_naissance, pays_origine)
    -> VALUES("Chat", "Mammifere", 2, "23-10-2005", "France");


INSERT INTO cage(capacite, superficie, capacite_max)
    -> VALUES("2", "10", "2");
INSERT INTO cage(capacite, superficie, capacite_max)
    -> VALUES("2", "50", "4");"""


import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mdp",
    database="zoo"
)

class Zoo:
    def __init__(self):
        self.cursor = db.cursor()
    
    def ajouter(self):
        self.display()
        while True:
            try:
                print("\nQue voulez-vous ajouter ?")
                print("1. Un animal")
                print("2. Une cage")
                choix = int(input("Votre choix : "))

                if choix == 1:
                    print("\nAjout d'un nouvel animal")
                    nom = str(input("Nom : "))
                    race = str(input("Race : "))
                    id_type_cage = int(input("ID de la cage : "))
                    date_naissance = input("Date de naissance (xx-xx-xxxx) : ")
                    pays_origine = str(input("Pays d'origine : "))

                    self.cursor.execute(
                        "INSERT INTO animal(nom, race, id_type_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)",
                        (nom, race, id_type_cage, date_naissance, pays_origine))
                    db.commit()
                    print("Nouvel animal ajouté avec succès !")

                elif choix == 2:
                    print("\nAjout d'une nouvelle cage")
                    capacite = int(input("Capacité de la cage : "))
                    superficie = int(input("Superficie de la cage : "))
                    capacite_max = int(input("Capacité maximale de la cage : "))

                    self.cursor.execute(
                        "INSERT INTO cage(capacite, superficie, capacite_max) VALUES (%s, %s, %s)",
                        (capacite, superficie, capacite_max)
                    )
                    db.commit()
                    print("Nouvelle cage ajoutée avec succès !")

                else:
                    print("Choix invalide.")

                self.display()
                break

            except mysql.connector.Error as err:
                print(f"Erreur SQL : {err}")
            except ValueError:
                print("Entrez des valeurs valides...")

    def supprimer(self):
        self.display()
        while True:
            try:
                print("\nQue voulez-vous supprimer ?")
                print("1. Un animal")
                print("2. Une cage")
                choix = int(input("Votre choix : "))

                if choix == 1:
                    id_suppr = int(input("\nEntrez l'ID de l'animal à supprimer : "))

                    self.cursor.execute("SELECT id FROM animal WHERE id = %s", (id_suppr,))
                    result = self.cursor.fetchone()

                    if result:
                        self.cursor.execute("DELETE FROM animal WHERE id = %s", (id_suppr,))
                        db.commit()
                        print("Animal supprimé avec succès !")
                    else:
                        print("Aucun animal trouvé avec cet ID.")

                elif choix == 2:
                    id_cage = int(input("\nEntrez l'ID de la cage à supprimer : "))

                    self.cursor.execute("SELECT id FROM cage WHERE id = %s", (id_cage,))
                    result = self.cursor.fetchone()

                    if result:
                        self.cursor.execute("DELETE FROM cage WHERE id = %s", (id_cage,))
                        db.commit()
                        print("Cage supprimée avec succès !")
                    else:
                        print("Aucune cage trouvée avec cet ID.")

                else:
                    print("Choix invalide.")

                self.display()
                break

            except mysql.connector.Error as err:
                print(f"Erreur SQL : {err}")
            except ValueError:
                print("Entrez des valeurs valides...")


    def modifier(self):
        self.display()
        while True:
            try:
                print("\nModification des informations")
                print("1. Modifier un animal")
                print("2. Modifier une cage")
                choix = int(input("Votre choix : "))

                if choix == 1:
                    id_animal = int(input("\nEntrez l'ID de l'animal à modifier : "))

                    # Vérifier si l'animal existe
                    self.cursor.execute("SELECT * FROM animal WHERE id = %s", (id_animal,))
                    result = self.cursor.fetchone()

                    if result:
                        print("\nQue souhaitez-vous modifier ?")
                        print("1. Nom")
                        print("2. Race")
                        print("3. ID de la cage")
                        print("4. Date de naissance")
                        print("5. Pays d'origine")
                        modif_choix = int(input("Votre choix : "))

                        champs = ["nom", "race", "id_type_cage", "date_naissance", "pays_origine"]
                        if 1 <= modif_choix <= 5:
                            nouvelle_valeur = input(f"Nouvelle valeur pour {champs[modif_choix - 1]} : ")

                            if modif_choix == 3:  # Vérification que l'ID de la cage est un entier
                                nouvelle_valeur = int(nouvelle_valeur)

                            self.cursor.execute(f"UPDATE animal SET {champs[modif_choix - 1]} = %s WHERE id = %s",
                                                (nouvelle_valeur, id_animal))
                            db.commit()
                            print("Informations de l'animal mises à jour avec succès !")
                        else:
                            print("Choix invalide.")
                    else:
                        print("Aucun animal trouvé avec cet ID.")

                elif choix == 2:
                    id_cage = int(input("\nEntrez l'ID de la cage à modifier : "))

                    # Vérifier si la cage existe
                    self.cursor.execute("SELECT * FROM cage WHERE id = %s", (id_cage,))
                    result = self.cursor.fetchone()

                    if result:
                        print("\nQue souhaitez-vous modifier ?")
                        print("1. Capacité")
                        print("2. Capacité maximale")
                        modif_choix = int(input("Votre choix : "))

                        if modif_choix == 1:
                            nouvelle_capacite = int(input("Nouvelle capacité : "))
                            self.cursor.execute("UPDATE cage SET capacite = %s WHERE id = %s", (nouvelle_capacite, id_cage))
                        elif modif_choix == 2:
                            nouvelle_capacite_max = int(input("Nouvelle capacité maximale : "))
                            self.cursor.execute("UPDATE cage SET capacite_max = %s WHERE id = %s", (nouvelle_capacite_max, id_cage))
                        else:
                            print("Choix invalide.")
                            return

                        db.commit()
                        print("Informations de la cage mises à jour avec succès !")

                    else:
                        print("Aucune cage trouvée avec cet ID.")

                else:
                    print("Choix invalide. Veuillez entrer 1 ou 2.")

                break  # Sortir de la boucle après modification réussie

            except mysql.connector.Error as err:
                print(f"Erreur SQL : {err}")
            except ValueError:
                print("Entrez une valeur valide.")


    def display(self):
        print("\nAnimaux :")
        self.cursor.execute("SELECT * FROM animal")
        for row in self.cursor.fetchall():
            print(row)  # Affichage des résultats

        print("\nCages :")
        self.cursor.execute("SELECT * FROM cage")
        for row in self.cursor.fetchall():
            print(row)  # Affichage des résultats

    def calculate_sup(self):
        self.cursor.execute("SELECT SUM(superficie) FROM cage")
        for row in self.cursor.fetchall():
            superficie = int(row[0])
            print(f"La superficie total des cages du zoo est de {superficie}m2.")

    def __del__(self):
        self.cursor.close()
        db.close()




def main():
    zoo = Zoo()
    while True:
        print("\n< - - - MENU - - - >")
        print("1. Ajouter un animal ou une cage")
        print("2. Supprimer un animal ou une cage")
        print("3. Modifier les infos d'un animal ou d'une cage")
        print("4. Afficher les animaux du zoo et la liste des animaux en cage")
        print("5. Superficie totale des cages")
        print("6. Quitter le menu")

        choice = int(input("\nVotre choix : "))

        if 1<=choice<=6:
            if choice == 1:
                zoo.ajouter()
            elif choice == 2:
                zoo.supprimer()
            elif choice == 3:
                zoo.modifier()
            elif choice == 4:
                zoo.display()
            elif choice == 5:
                zoo.calculate_sup()
            elif choice == 6:
                print("Fermeture de l'application...\n")
                exit()
        else:
            print("Entrée invalide, entrez un chiffre entre 1 et 6")



if __name__ == "__main__":
    main()