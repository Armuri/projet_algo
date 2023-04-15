import json
from json import JSONEncoder

class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__  

class Livre:
    def __init__(self, titre, auteur, id, disponible):
        self.titre = titre
        self.auteur = auteur
        self.id = id
        self.disponible = disponible=='True'

    def presentation(self):
        return str(self.id) + ' - ' + self.titre + ' - ' + self.auteur
    

def reservation(number):
    f = open("testlivre.json", "r")
    data = json.load(f)
    books =[]
    i=1
    for b in data:
        books.append(Livre(b['titre'],b['auteur'], i,b['disponible']))
        i = i + 1

    books[int(number) - 1].disponible = False
    f.close()

    f = open("livres2.json", "w")
    f.write(json.dumps(books, cls=MyEncoder, indent=4, sort_keys=books[int(number) - 1].disponible, ensure_ascii=False))
    
def ajoutLivre(auteur,id,disponible,titre):
    f = open("testlivre.json", "r")
    data = json.load(f)
    books =[]
    for b in data:
        books.append(Livre(b['auteur'],b['id'],b['disponible'],b['titre']))
    f.close()
    
    newBook = {
        "auteur" : auteur,
        "id" : id,
        "disponible" : disponible,
        "titre" : titre
    }
    
    f = open("test.json", "w")
    f.write(json.dumps(newBook, cls=MyEncoder, indent=4))
    
def modifLivre(id, titre, auteur, disponible):
    print(id, titre, auteur, disponible)
    print("code marche pas mais nous avons réalisé la démarche de réflexion.")
    # f = open("testlivre.json", "r")
    # data = json.load(f)
    # books =[]
    # for b in data:
    #     books.append(Livre(b['auteur'],b['id'],b['disponible'],b['titre']))
    
    # books[int(id) - 1].titre = titre
    # books[int(id) - 1].auteur = auteur
    # f.close()
    
    # f = open("livres2.json", "r+")
    # f.write(json.dumps(books, cls=MyEncoder, indent=1, sort_keys=books[int(id) - 1], ensure_ascii=titre))
    # f.write(json.dumps(books, cls=MyEncoder, indent=1, sort_keys=books[int(id) - 1], ensure_ascii=auteur))
    
def suppLivre():  
    new_data = []
    with open("testlivre.json", "r") as f:
        data = json.load(f)
        data_length = len(data)
    delete_option = input(f"Select a number 0-{data_length}: ")
    # iterate over i and data simultaneously
    for i, entry in enumerate(data):
        if i != int(int(delete_option) -1):
            new_data.append(entry)

    with open("livres2.json", "w") as f:
        json.dump(new_data, f, indent=4)