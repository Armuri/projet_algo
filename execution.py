import livres
import utilisateurs
import gestionlivre
import gestionutilisateur

while(True):
    a = input("Quel est le type d'utilisateur ? " '\n'
              "1 - Utilisateur" '\n'
              "2 - Gestionnaire" '\n'
              "3 - Quitter l'interface" '\n')
    if a == "1":
        util = input("Bienvenue sur l'espace utiisateur, quelle action voulez-vous réaliser ?" '\n'
                     "1 - Voir l'ensemble des livres disponibles" '\n' 
                     "2 - Quitter l'interface" '\n')
        if util == "1":
            livres.AfficheLivre()
            reserv_util = input("Voulez-vous réserver un livre ?"'\n'
                                "1 - Oui" '\n'  
                                "2 - Non, quitter l'interface" '\n' )
            if reserv_util == "1":
                auth_util = input("Avez-vous un compte ?"'\n'
                                  "1 - Oui" '\n' 
                                  "2 - Non, quitter l'interface" '\n')
                if auth_util == "1":
                    utilisateurs.auth_utilisateur()
                    livres.AfficheLivreDisp()
                    reserv_util1 = input("Parmi les livres disponibles, entrer le numéro du livre "'\n'
                                         "Q - Quitter l'interface"'\n')
                    gestionlivre.reservation(reserv_util1)
                    # utilisateurs.reservation()
                    print("Votre réservation a été prise en compte")
                    break
                else:
                    break
            else:
                break    
        else:
            break
    elif a == "2":
        admin = input("Bienvenue sur l'espace Gestionnaire, que souhaitez-vous faire ? " '\n'
                      "1 - Voir tous les utilisateurs"'\n'
                      "2 - Voir tous les livres"'\n'
                      "3 - Quitter l'interface"'\n')
        if admin == "1":
            utilisateurs.AfficheAllUtilisateur()
            super_util = input("Voulez-vous réaliser une action sur les utilisateurs ? "'\n'
                               "1 - Oui"'\n'
                               "2 - Non, quitter l'interface"'\n')
            if super_util =="1":
                super_util1 = input("Quelle action voulez-vous réaliser ?"'\n'
                                    "1 - Ajouter un utilisateur"'\n'
                                    "2 - Modifier un utilisateur"'\n'
                                    "3 - Supprimer un utilisateur"'\n'
                                    "4 - Quitter l'interface"'\n')
                if super_util1 =="1":
                    nom = input("Nom d'utilisateur : ")
                    prenom = input("Prénom d'utilisateur : ")
                    age = input("Age de l'utilisateur : ")
                    adresse_email = input("L'adresse email de l'utilisateur : ")
                    type = input("Type d'utilisateur : ")
                    gestionutilisateur.ajoutUtilisateur(nom,prenom,age,adresse_email,type)
                    utilisateurs.AfficheAllUtilisateur()
                    ("Ajout apporté avec succès")
                    break
                elif super_util1 =="2": 
                    nom = input("Nom d'utilisateur : ")
                    prenom = input("Prénom d'utilisateur : ")
                    age = input("Age de l'utilisateur : ")
                    adresse_email = input("L'adresse email de l'utilisateur : ")
                    type = input("Type d'utilisateur : ")
                    gestionutilisateur.ajoutUtilisateur(nom,prenom,age,adresse_email,type)
                    utilisateurs.AfficheAllUtilisateur()
                    ("Modifications apportées avec succès")
                    break
                elif super_util1 =="3":
                    gestionutilisateur.suppUtilisateur()
                    utilisateurs.AfficheAllUtilisateur()
                    ("Suppression réalisée avec succès")
                    break
                else:
                    break
            else:
                break
        elif admin == "2":
            print("Voici l'ensemble des livres répertoriés dans la bibliothèque : "'\n')
            livres.AfficheLivreDisp()
            livre_admin = input("Quelle action voulez vous réaliser sur les livres ?"'\n'
                                "1 - Ajouter un livre"'\n'
                                "2 - Modifier un livre"'\n'
                                "3 - Supprimer un livre"'\n'
                                "4 - Quittez l'interface"'\n')
            if livre_admin =="1":
                auteur1 = input('Auteur du : ')
                id1 = input('id du livre : ')
                dispo1 = input('Disponibilité : ')
                titre1 = input('Titre du livre : ')
                gestionlivre.ajoutlivre(auteur1, id1,dispo1,titre1)
                livres.AfficheLivre()
                print("Le Livre a été ajouté avec succès")
                break
            elif livre_admin == "2":
                livres.AfficheLivre()
                id = input('id du livre : ')
                titre = input('Titre du livre : ')
                auteur = input('Auteur du livre : ')
                disponible = True
                gestionlivre.modifLivre(id,titre,auteur,disponible)
                livres.AfficheLivre()
                print("Le Livre a été modifié avec succès")
                break
            elif livre_admin == "3":
                livres.AfficheLivre()
                gestionlivre.suppLivre()
                livres.AfficheLivre()
                print("Suppression du livre effectué avec succès ! ")
                break
            else:
                break
    else:
        break

    