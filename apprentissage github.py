# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 15:08:00 2025

@author: chall
"""

# Commande de base 

# pwd   donner le chemin qu'on utilise

# cd nomemplacement  permet d'accéder à un espace 
# EX: cd desktop

# créer un dossier 
# mkdir github

# enoncer une liste d'un dossier
# ls à l'intérieur du dossier 

# créer un fichier dans un dossier
# touch nomfichier.formatfichier
 
#revenir en arriere
#cd ..

#envoie information compte
#gitconfig --global--list

# initialiser le depot en local
#git init

# ajoute d'un cout toute les version
# du projet le . signifie tout
# git add .

#créer un nouveau commit contenant les fichiers
# mis en index par add .
#git commit -m "Explication"

# afficher toute les versions
# git log
# git log -n2 affiche les deux derniers commit

# affiche le détail du dernier commit
# git show
# git show IDcommit  affiche le detail du commit 
# q     pour fermer le prompt

#revenir a une version antérieure
# git checkout celle précedante
# git checkout IDcommit remet version du commit demander

#créer un dossier avec le repertory créer sur github 
# git clone IDrepertory

#enregistrer dans github
#git push-u origin nombranche


#retenir pour enregistrer dossier
#git add .
#git commit -m "explication"
#git push -u origin nombranche