import random
import os

# GENERATEUR DE LISTE ALEATOIRE DE PLUS DE 16 INDENTITES POUR EXEMPLE

#liste des noms prealable
liste_nom = ['Aaron', 'Getler', 'Sala', 'Kane', 'Poutine', 'Macron', 'harry', 'Kalvin', 'Edenberg', 'Mané', 'Trump', 'Verdez', 'Montiel', 
'Mbenza', 'Sasu', 'knyata','Ntelo', 'Nka', 'Bertrand', 'lelouche', 'Jong un', 'yong', 'Watara', 'Biya', 'Borne', 'De Jong', 'Luca', 'Trevor', 'Zing',
'kabika', 'Kabila', 'Kevin', 'Tshisekedi', 'Mobutu', 'Lorenso', 'Kim', 'Kardashan', 'Kanye', 'Mudimbe', 'Biden', 'Obama']

#liste des presnoms
liste_prenom = ['Aaron', 'David', 'Emmanuel', 'Elie', 'Christian', 'Jonathan', 'Junior', 'William', 'Yves', 'jean', 'jean-pierre', 
'pierre', 'Paul', 'Rubain', 'Ivar', 'Daniel', 'James', 'Donald', 'Carlos', 'Albert', 'Emery', 'Felix',
'Dav', 'Ruffin', 'Orphe', 'Ben', 'Joel',  'Rex', 'Marcel', 'Si', 'Benedicte', 'Barack', 'Franck', 'Eden', 'Jordan', 'levis']

for i in range(16): #nombre d'enregitrement dans la liste ici 16 dans notre cas
    n = random.choices(liste_nom)
    prn = random.choices(liste_prenom)

    nom = "".join(str(j)for j in n) #filtre et extraction de chaque nom
    prenom = "".join(str(v)for v in prn) #filtre et extraction des presnoms

#Enregistrement dans le fichiers csv
    with open('liste.csv', 'r+') as f:
        listeinfos = f.readlines()
        personnes = []
        for line in listeinfos:
            entrees = line.split(',')
            personnes.append(entrees[0])
        if nom and  prenom not in personnes:
            f.writelines(f'\n{nom},{prenom}') #affectation des colonnes et valeurs


