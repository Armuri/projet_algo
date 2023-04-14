import livres 
import utilisateurs 


a = input('1 = utilisateurs ou  2 = gestionnaire/admin ? \n')
if a == str(1) : 
    util = input('Bienvenue utilisateur/utilisatrice, écrivez 1 pour consulter les livres disponibles et 2 pour la gestion de votre compte \n')
    if util == str(1):
        livres.loadBook()
        util1 = input("Ecrivez 1 pour réserver un livre s'il vous plaît \n")
else:
    admin = input('Bienvenue gestionnaire/admin, écrivez 1 pour consulter la liste des utilisateurs \n')
    if admin == str(1):
        print(utilisateurs)
        admin1 = input('Ecrivez 1 pour ajouter un utilisateur, 2 pour modifier un utilisateur et 3 pour supprimer un utilisateur \n')
        if admin1 == str(1) :
            a1 = input('Auteur du livre : ')
            t1 = input('Titre du livre : ')
            e1 = input('Editeur du livre : ')
            a2 = input('Année de parution : ')
            g1 = input('Genre du livre : ')
            print(a1 + ' ' + t1 + ' ' + e1 + ' ' + a2 + ' ' + g1)
            # create_utilisateur() 
        elif admin1 == str(2):
            print('en cours de développement')
        elif admin1 == str(3):
            print('en cours de développement')
    else:
        print('Erreur de syntaxe : veuillez recommencer')
        # break
             
# if self.type =='etudiant':
#     l'étudiant ne peut posséder uniquement 3 livres

# if self.type =='enseignant':
#     l'enseignant peut posséder infini livre (sans limite)

# if self.type =='normal':
#     l'utilisateur normal ne peut posséder uniquement que 2 livres.