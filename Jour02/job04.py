# Job 04 : Récupérer les noms et capacités de la table salle

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdp",
    database="laplateforme"
)

cursor = db.cursor()

# Exécution de la requête pour récupérer les données
cursor.execute("SELECT nom, capacite FROM salle")

list = []
# Récupération et affichage des résultats
rows = cursor.fetchall()
for row in rows:
    list.append(row)

print(list)

# Fermeture de la connexion
cursor.close()
db.close()