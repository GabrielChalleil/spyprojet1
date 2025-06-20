


help(round)

help(round(-2.01))

help(abs)

def pls_petite_diff(a,b,c):
    """Return the smallest difference between any two numbers
    among a, b and c."""
    
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1,diff2,diff3)

help(pls_petite_diff)




def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    # fn défini une fonction et arg un argument
    return fn(arg)

def squared_call(fn, arg):
    # fn défini une fonction et arg un argument
    return fn(fn(arg))

print(
    call(mult_by_five, 10),
    squared_call(mult_by_five,10), 
    sep='\n', # '\n' is the newline character - it starts a new line
)




print(1,2,3, sep='<') #if there is no sep the default value is a space

x= True
print (x)
print(type(x))

# pour utiliser un boléen il faut poser == ou >= qui 
# signifie strict égal ou strict sup/inf 
def can_run_for_president(age):
    """Can someone of the given age run for president in the US?"""
    return age >= 35

print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))


#longueur d'une liste
objet =[1,2,3,4,5]
len(objet)
# remettre par ordre alphabétique
sorted(planets)
# somme des valeurs de la suite
sum(objet)

# mettre une apostrophe
'l\'arbre'
#%%
if condition1:
    # bloc 1
elif condition2:
    # bloc 2
else:
    # bloc 3

#while pour faire des répétions jusqu'à ce que la condition soit respecté
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue  # saute l'affichage quand i vaut 3
    print("i =", i)
else:
    print("Boucle finie")


#utilisation de la boucle for pour faire des décomptes
for i in range(5):
    if i == 2:
        continue
    print(i)


#utilisation de la boucle for pour faire des énumérations
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print("J’aime les", fruit)

i=0
while i<10:
    print(i, end='')
    i+=1

#%%

#Définir une fonction 

def nom_de_la_fonction(paramètres):
    # instructions
    retun résultat

#paramètre est composé des variables utilisé par la fonction

#EX:
def presenter_personne(prenom, age, ville):
    print(f"Bonjour, je m'appelle {prenom}, j'ai {age} ans et je vis à {ville}.")

presenter_personne("Lina", 25, "Paris")
presenter_personne("Karim", 30, "Lyon")

# un tuple est une liste de donnée dans une variable
# on peut avoir des listes de tuples dans un variable

#EX

# Une liste de tuples contenant des prénoms et noms
mon_tuple = [("Gabriel", "Dupont"), ("Alice", "Martin"), ("Julien", "Bernard")]

# Accéder à un élément spécifique (premier tuple)
print(mon_tuple[0])  # Affiche ("Gabriel", "Dupont")
print(mon_tuple[-1]) #affiche la derniere liste
print(mon_tuple[0:2]) # affiche de 0 à 2
print(mon_tuple[2:] # affiche jusqu'à la fin

#remplacer une valeur
mon_tuple[1] = 'Henry'

# Accéder à un prénom spécifique
print(mon_tuple[1][0])  # Affiche "Alice"

# ajouter un truc à la fin
mon_tuple.append('Pluto')

# retire et affiche le dernier element
mon_tuple.pop()

# affiche l'ordre de l'élément que tu cherche
mon_tuple.index('Earth')

# savoir si un élément est dans une liste
"Earth" in planets

# Parcourir la liste et afficher les noms complets
for prenom, nom in mon_tuple:
    print(f"{prenom} {nom}")

Question = ["quel date est née Napoléon", "comment s'appelait la femme de napoléon ","combien d'enfant avait Napoléon"]
réponse_juste = ["1785", "Amelia","5"]
réponse = []
for i in range(len(question)):
    reponse_donnee = input(question[i])  # Pose la question
    if reponse_donnee.lower() == reponses_justes[i].lower():
        print("bonne réponse.")
    else:
        print("mauvaise reponse")

for element in Question:
    print("element")
    def question1

#%% dictionnaire

#associer une une valeur ou un mot à un mot clé 

# Création d’un dictionnaire
mon_dico = {"nom": "Gabriel", "âge": 30, "ville": "Marseille"}

# Accéder à une valeur
print(mon_dico["nom"])  # Affichera "Gabriel"

# Ajouter ou modifier une valeur
mon_dico["âge"] = 31
mon_dico["pays"] = "France"

# Supprimer une entrée
del mon_dico["ville"]

# Vérifier si une clé existe
if "nom" in mon_dico:
    print("La clé 'nom' existe !")

# Parcourir un dictionnaire
for cle, valeur in mon_dico.items():
    print(cle, ":", valeur)

#%% Module
import math

print("It's math! It has type {}".format(type(math)))

#sous module
# un sous module est une sous partie du module qui contien elle meme des fonctions

import numpy

# Générer 10 nombres aléatoires entre 1 et 6 (comme des dés)
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)

# on utilise deux points











