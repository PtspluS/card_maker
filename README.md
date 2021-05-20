# Comment l'utiliser

## Ajouter une carte 
* Rajouter la carte au csv `card.csv`en complettant les champs.

## Ajouter un type de carte
* Rajouter dans le fichier `config.json` le nom du type de carte et le chemin vers le template de la carte.

## Ajouter un template de carte
* Ajouter dans le dossier `./template/` la template de la carte au format html suivant :

| Nom de l'alias | Correspondance | Exemple |
|:--------------:|:--------------:| :-------|
| {{title}} | Titre de la carte | Tempête d'astéroïdes |
| {{text}} | Le text a afficher sur la carte | Endommage les ventillations des salles |
| Exclusif au pièces | ---------------- |------------------------------------------|
| {{cost}} | Le coup de la pièce | |
| {{places}} | Nombre de places dans la pièces | |
| {{subtype}} | Le sous type de la pièce | |

Le fichier html doit contenir assez de places pour mettre 9 cartes au format 8,9 cm par 6,4 cm soit un carré de 3*3.

* Ajouter dans le fichier `config.json` le nom du type de carte et le chemin vers le template de la carte nouvellement créé.

## Ajouter une illustration 

* Ajouter l'ilustration dans le dossier correspondant au type de la carte dans `./img/`.
* Ajouter le chemin vers l'illustration dans le fichier `./cards.csv` pour la carte correspondante.

## Changer une carte

* Il suffit de modifier le fichier `./cards.csv` pour modifier les données d'une carte.

## Créer les planches d'impression 

* Le script charge le fichier `./cards.csv` et créé tout seul les fichiers pdf correpondants au planche d'impression.

