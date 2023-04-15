import json
from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__  
    
class Utilisateur : 
    def __init__(self,nom, prenom, adresse_email, type, livres):
        self.nom = nom
        self.prenom = prenom
        self.adresse_email = adresse_email
        self.type = type
        self.livres = livres
        
    def presentation(self):
        return self.nom  + '\n' + self.prenom  + '\n' + self.adresse_email + '\n' +  self.type + '\n' + str(self.livres)
    

def ajoutUtilisateur(id,nom,prenom,age,adresse_email,type):
    f = open("testlivre.json", "r")
    data = json.load(f)
    utilisateurs =[]
    livre =[]
    for b in data:
        utilisateurs.append(Utilisateur(b['id'],b['nom'],b['prenom'],b['age'],b['adresse_email'],b['type'],b['livre']))
    f.close()
    
    newUser = {
        "id" : id,
        "nom" : nom,
        "prenom" : prenom,
        "age" : age,
        "adresse_email" : adresse_email,
        "type" : type,
        "livre" : livre
    }
    
    f = open("test.json", "w")
    f.write(json.dumps(newUser, cls=MyEncoder, indent=4))

def modifUtilisateur(id, titre, auteur, disponible):
    print(id, titre, auteur, disponible)
    print("code marche pas mais nous avons réalisé la démarche.")
    # f = open("testutilisateur.json", "r")
    # data = json.load(f)
    # utilisateurs =[]
    # for b in data:
    #     utilisateur.append(Utilisateur(b['id'],b['nom'],b['prenom'],b['age'],b['adresse_email'],b['type'],b['livre']))
    # newUser = {
    #     "id" : id,
    #     "nom" : nom,
    #     "prenom" : prenom,
    #     "age" : age,
    #     "adresse_email" : adresse_email,
    #     "type" : type,
    #     "livre" : livre
    # }
    # f.close()
    
    # f = open("livres2.json", "r+")
    # f.write(json.dumps(utilisateur, cls=MyEncoder, indent=1, sort_keys=utilisateur[int(id) - 1], ensure_ascii=newUser))


def suppUtilisateur():  
    new_data = []
    with open("testutilisateurs.json", "r") as f:
        data = json.load(f)
        data_length = len(data)
    delete_option = input(f"Select a number 0-{data_length}: ")
    # iterate over i and data simultaneously
    for i, entry in enumerate(data):
        if i != int(int(delete_option) -1):
            new_data.append(entry)

    with open("utilisateurs2.json", "w") as f:
        json.dump(new_data, f, indent=4)