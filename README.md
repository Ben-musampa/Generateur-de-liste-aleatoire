# Générateur de Liste Aléatoire d'Identités
Ce script Python permet de générer une liste aléatoire de plus de 16 pour code.py et  1000 identités pour 1000.py en combinant
des noms et prénoms aléatoires. Les identités sont ensuite enregistrées dans un fichier CSV
nommé `liste.csv`.
## Prérequis
Le script ne nécessite aucune dépendance externe. Assurez-vous simplement d'avoir Python
installé sur votre système.
## Utilisation
1. Personnalisation des noms et prénoms : Vous pouvez personnaliser la liste des noms et la liste
des prénoms en modifiant les listes `liste_nom` et `liste_prenom` respectivement. Ajoutez ou
supprimez des noms/prénoms selon vos besoins.
2. Génération des identités : Le script génère plus de 1000 identités aléatoires en combinant
aléatoirement un nom et un prénom. Vous pouvez modifier le nombre d'enregistrements en
modifiant la valeur de la boucle `for i in range(1000)` selon vos besoins.
3. Exécution du script : Pour exécuter le script, ouvrez un terminal ou une invite de commande et
exécutez la commande suivante :
```
python nom_du_script.py
```
4. Résultats : Après l'exécution du script, un fichier CSV nommé `liste.csv` sera créé dans le
répertoire du script. Ce fichier contiendra la liste des identités générées au format "Nom,
Prénom" sur chaque ligne.
## Format du fichier CSV
Le fichier CSV généré aura le format suivant :
```
Nom, Prénom
Aaron, David
...
```
Chaque ligne du fichier correspondra à une identité générée.
## Remarques
- Le script sélectionne les noms et prénoms aléatoirement à partir des listes prédéfinies.
Assurez-vous d'ajuster ces listes selon vos préférences ou besoins.
- Le script vérifie automatiquement si le fichier `liste.csv` existe déjà dans le répertoire. S'il
existe, il sera écrasé par la nouvelle liste générée.
- Vous pouvez personnaliser ce script en ajoutant des fonctionnalités supplémentaires, comme
la génération d'autres informations aléatoires (âge, adresse, etc.), selon vos besoins.
---
Assurez-vous de remplacer "nom_du_script.py" par le nom réel de votre fichier Python. Ce
README fournit des instructions pour utiliser le script et personnaliser les données générées.
Vous pouvez également ajouter plus d'informations, d'exemples ou de captures d'écran pour
rendre le README plus complet et informatif.
