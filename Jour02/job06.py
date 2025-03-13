# Job 06 : Capacité totale de toutes les salles

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdp",
    database="laplateforme"
)

cursor = db.cursor()

# Exécution de la requête pour récupérer les données
cursor.execute("SELECT SUM(capacite) FROM salle")

# Récupération et affichage des résultats
rows = cursor.fetchall()
for row in rows:
    capacite_total = int(row[0])
    print(f"La capacité de toutes les salles est de : {capacite_total}")

# Fermeture de la connexion
cursor.close()
db.close()