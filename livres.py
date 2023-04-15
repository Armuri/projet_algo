import json

class Livre : 
    def __init__(self,auteur, id, disponible, titre):
        self.auteur = auteur
        self.id = id
        self.disponible = disponible
        self.titre = titre
        
    def Presentation(self):
        return str(self.id) + ' - ' + self.titre + " écrit par : " + self.auteur
    
    def Disponible(self):
        if self.disponible == True :
            return str(self.id) + ' - ' + self.titre + " de " + self.auteur + " est disponible "
        else:
            return str(self.id) + ' - '+ self.titre + "de " + self.auteur + " est indisponible"

def AfficheLivre():        
    f = open("livres2.json", "r")
    content = json.load(f)
    tab = []
    for d in content:
        tab.append(Livre(d['auteur'],d['id'],d['disponible'],d['titre']))
    for livre in tab:
        print(Livre.Presentation(livre))
        
def AfficheLivreDisp():        
    f = open("livres2.json", "r")
    content = json.load(f)
    tab = []
    for d in content:
        tab.append(Livre(d['auteur'],d['id'],d['disponible'],d['titre']))

    for livre in tab:
        print(Livre.Disponible(livre))

        
