# Job 01 : Connecter par pyhton à la database et afficher le contenu

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdp",
    database="laplateforme"
)

cursor = db.cursor()

if db.is_connected():
    print("Connexion réussie")

# Exécution de la requête pour récupérer les données
cursor.execute("SELECT * FROM etudiant")

# Récupération et affichage des résultats
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fermeture de la connexion
cursor.close()
db.close()