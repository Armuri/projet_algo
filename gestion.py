import json

# Charge les données JSON
with open('utilisateurs.json') as f:
    utilisateurs = json.load(f)

while True:
    action = input("Que souhaitez-vous faire ? (1: afficher un utilisateur, 2: ajouter un utilisateur, 3: supprimer un utilisateur, q: quitter)")

    if action == "1":
        nom_utilisateur = input("Entrez le nom de l'utilisateur que vous souhaitez afficher : ")
        for utilisateur in utilisateurs:
            if utilisateur['nom'] == nom_utilisateur:
                print(utilisateur)
                break
        else:
            print("Utilisateur non trouvé")

    elif action == "2":
        nouvel_utilisateur = {}
        nouvel_utilisateur['nom'] = input("Entrez le nom de l'utilisateur : ")
        nouvel_utilisateur['prénom'] = input("Entrez le prénom de l'utilisateur : ")
        nouvel_utilisateur['age'] = int(input("Entrez l'âge de l'utilisateur : "))
        nouvel_utilisateur['adresse email'] = input("Entrez l'adresse email de l'utilisateur : ")
        nouvel_utilisateur['type'] = input("Entrez le type d'utilisateur : ")
        nouvel_utilisateur['livres'] = []
        utilisateurs.append(nouvel_utilisateur)
        print("Utilisateur ajouté avec succès")

    elif action == "3":
        nom_utilisateur = input("Entrez le nom de l'utilisateur que vous souhaitez supprimer : ")
        for utilisateur in utilisateurs:
            if utilisateur['nom'] == nom_utilisateur:
                utilisateurs.remove(utilisateur)
                print("Utilisateur supprimé avec succès")
                break
        else:
            print("Utilisateur non trouvé")

    elif action == "q":
        # Enregistrement
        with open('utilisateurs.json', 'w') as f:
            json.dump(utilisateurs, f)
        print("Au revoir !")
        break

    else:
        print("Action invalide")
# Enregistrer les modifications apportées dans le fichier JSON
with open('utilisateurs.json', 'w') as f:
    json.dump(utilisateurs, f)
