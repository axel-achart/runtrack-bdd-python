# Job 05 : Calculer la superficie de l'ensemble des étages

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mdp",
    database="laplateforme"
)

cursor = db.cursor()

# Exécution de la requête pour récupérer les données
cursor.execute("SELECT SUM(superficie) FROM etage")

# Récupération et affichage des résultats
rows = cursor.fetchall()
for row in rows:
    superficie_total = int(row[0])
    print(f"La superficie de La Plateforme est de {superficie_total} m2")

# Fermeture de la connexion
cursor.close()
db.close()