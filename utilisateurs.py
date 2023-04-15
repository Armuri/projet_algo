import json

class Utilisateur : 
    def __init__(self,nom, prenom, adresse_email, type, livres):
        self.nom = nom
        self.prenom = prenom
        self.adresse_email = adresse_email
        self.type = type
        self.livres = livres
        
    def presentation(self):
        return self.nom  + '\n' + self.prenom  + '\n' + self.adresse_email + '\n' +  self.type + '\n' + str(self.livres)
    
    def verifuser(self):
        return "Content de vous revoir " + self.nom 
    
    

def AfficheAllUtilisateur():  
    f = open("utilisateurs2.json", "r")
    content = json.load(f)
    tab = []
    for d in content:
        tab.append(Utilisateur(d['nom'],d['prenom'],d['adresse_email'],d['type'],d['livres']))
    for user in tab:
        print(Utilisateur.presentation(user)) 
        
def auth_utilisateur():
    f = open("utilisateurs2.json", "r")
    content = json.load(f)
    tab=[]
    nom_utilisateur = input("Entrez votre nom : ")
    for utilisateur in content:
        if utilisateur['nom'] == nom_utilisateur:
            tab.append(Utilisateur(utilisateur['nom'],utilisateur['prenom'],utilisateur['adresse_email'],utilisateur['type'],utilisateur['livres']))
            for user in tab:
                print(Utilisateur.verifuser(user))
        else:
            StopIteration   
        



            
