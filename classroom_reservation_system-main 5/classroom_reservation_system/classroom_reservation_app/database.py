import sqlite3

# Se connecter à la base de données
conn = sqlite3.connect('db.sqlite3')

# Créer un curseur
cur = conn.cursor()

# Insérer des données dans une table
cur.execute("INSERT INTO batiment (nom) VALUES (ayoub)", ("valeur1", "valeur2"))

# Valider la transaction
conn.commit()

# Fermer la connexion
conn.close()