import json

class Livre : 
    def __init__(self,auteur, titre, editeur, annee, genre, disponible):
        self.auteur = auteur
        self.titre = titre
        self.editeur = editeur
        self.annee = annee
        self.genre = genre
        self.disponible = disponible
        
    def __str__(self):
        return "Ce livre est un/une : " + self.genre + " du nom de : " + self.titre + " écrit par : " + self.auteur + ',' " édité par : " + self.editeur + ' publié en : ' + str(int(self.annee)) + ' ' + self.disponible

def loadBook():        
    f = open("bibliolivres.json", "r")
    content = json.load(f)

    tab = []
    x=0
    for d in content:
        tab.append(Livre(d['auteur'],d['titre'],d['editeur'],d['annee'],d['genre'],d['disponible']))
    for livre in tab:
        print(livre) 
