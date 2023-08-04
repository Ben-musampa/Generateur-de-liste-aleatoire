import random
import os
# GENERATEUR DE LISTE ALEATOIRE DE PLUS DE 1000 IDENTITES
# Liste des noms prédéfinis
liste_nom = ['Aaron', 'Getler', 'Sala', 'Kane', 'Mbenza', 'Sasu', 'Knyata', 'Kabika', 'Kabila', 'Kevin',
'Ntelo', 'Nka', 'Bertrand', 'Poutine', 'Macron', 'Harry', 'Lelouche', 'Kalvin', 'Edenberg', 'Mané', 'Jong un', 'Yong',
'Trump', 'Verdez', 'Montiel', 'Tshisekedi', 'Mobutu', 'Lorenso', 'Kim', 'Kardashan', 'Watara', 'Kanye', 'Biya',
'Mudimbe', 'Borne', 'De Jong', 'Luca', 'Trevor', 'Zing', 'Biden', 'Obama']
# Liste des prénoms prédéfinis
liste_prenom = ['Aaron', 'David', 'Pierre', 'Paul', 'Emmanuel', 'Rubain', 'Ivar', 'Daniel', 'Elie',
'Christian', 'Jonathan', 'Junior', 'William', 'James', 'Donald', 'Dav', 'Ruffin', 'Orphe', 'Ben', 'Joel', 'Rex', 'Marcel',
'Si', 'Carlos', 'Albert', 'Emery', 'Yves', 'Jean', 'Jean-Pierre', 'Felix', 'Benedicte', 'Barack', 'Franck', 'Eden', 'Jordan', 'Levis']
# Génération et enregistrement des identités aléatoires dans le fichier CSV
with open('liste.csv', 'w') as f: # Utilisation du mode 'w' pour écraser le fichier s'il existe déjà
    for i in range(1000): # Générer plus de 1000 identités ici (nombre d'enregistrements)
        nom = random.choice(liste_nom)
        prenom = random.choice(liste_prenom)
        f.write(f'{nom}, {prenom}\n') # Enregistrement dans le fichier CSV (ajout de '\n' pour passer à la ligne suivante)
