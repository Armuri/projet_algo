import json

class Utilisateur : 
    def __init__(self,nom, prenom, adresse_email, type, livres):
        self.nom = nom
        self.prenom = prenom
        self.adresse_email = adresse_email
        self.type = type
        self.livres = livres
        
    def __str__(self):
        return self.nom  + '\n' + self.prenom  + '\n' + self.adresse_email + '\n' +  self.type + '\n' + str(self.livres)

def loadUser():  
    f = open("utilisateurs.json", "r")
    content = json.load(f)
    tab = []
    for d in content:
        tab.append(Utilisateur(d['nom'],d['prenom'],d['adresse_email'],d['type'],d['livres']))
    for user in tab:
        print(user)

