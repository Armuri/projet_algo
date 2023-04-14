import livres
import utilisateurs

while(True):
    a = input("Quel est le type d'utilisateur ? " '\n'
              "1 - Utilisateur" '\n'
              "2 - Administrateur" '\n'
              "3 - Quitter l'interface" '\n')
    if a == "1":
        util = input("Bienvenue sur l'espace utiisateur, quelle action voulez-vous réaliser ?" '\n'
                     "1 - Voir l'ensemble des livres disponibles" '\n' 
                     "2 - Quitter l'interface" '\n')
        if util == "1":
            livres.loadBook()
            reserv_util = input("Voulez-vous réserver un livre ?"'\n'
                                "1 - Oui" '\n' 
                                "2 - Non, quitter l'interface" '\n' )
            if reserv_util == "1":
                reserv_util1 = input("Parmi les livres disponibles, entrer le numéro du livre "'\n'
                                     "Q - Quitter l'interface"'\n')
                if reserv_util1 == "1" : 
                    # !!!!! à modifier !!!!!
                    print("Votre réservation a été prise en compte")
                    break
                else:
                    break
            else:
                break    
        else:
            break
    elif a == "2":
        admin = input("Bienvenue sur l'espace administrateur, que souhaitez-vous faire ? " '\n'
                      "1 - Voir tous les utilisateurs"'\n'
                      "2 - Voir tous les livres"'\n'
                      "3 - Quitter l'interface"'\n')
        if admin == "1":
            utilisateurs.loadUser()
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
                    # !!!!! à modifier !!!!!!
                    a2 = input("Nom d'utilisateur : ")
                    t2 = input("Prénom d'utilisateur : ")
                    e2 = input("Age de l'utilisateur : ")
                    a4 = input("Type d'utilisateur : ")
                    g2 = "Pas de livre"
                    print(a2 + ' ' + t2 + ' ' + e2 + ' ' + a4 + ' ' + g2)
                    break
                elif super_util1 =="2":
                    # !!!!! à modifier !!!!!!
                    ("Modifications apportées avec succès")
                elif super_util1 =="3":
                    # !!!!! à modifier !!!!!!
                    ("Suppressions réalisées avec succès")
                else:
                    break
            else:
                break
        elif admin == "2":
            livres.loadBook()
            livre_admin = input("Quelle action voulez vous réaliser sur les livres ?"'\n'
                                "1 - Ajouter un livre"'\n'
                                "2 - Modifier un livre"'\n'
                                "3 - Supprimer un livre"'\n'
                                "4 - Quittez l'interface"'\n')
            if livre_admin =="1":
                # !!!! à mofifier !!!!
                a1 = input('Auteur du livre : ')
                t1 = input('Titre du livre : ')
                e1 = input('Editeur du livre : ')
                a2 = input('Année de parution : ')
                g1 = input('Genre du livre : ')
                print(a1 + ' ' + t1 + ' ' + e1 + ' ' + a2 + ' ' + g1)
                break
            elif admin == "2":
                # !!!!! à modifier !!!!!
                modif_livre = input("Quelle livre voulez-vous modifier ?"'\n')
            elif admin == "3":
                # !!!!! à modifier !!!!!!
                supp_livre = input("Quelle livre voulez-vous supprimer ?"'\n'
                                   "Entrer le numéro du livre"'\n'
                                   "Q - Quitter l'interface"'\n')
                if supp_livre == int(supp_livre):
                    # !!!!! à modifier !!!!!!
                    print("Suppression du livre effectué avec succès ! ")
                elif supp_livre == "Q":
                    break
            else:
                break
    else:
        break

    