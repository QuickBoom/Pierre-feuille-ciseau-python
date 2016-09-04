import random
Pierre = 1
Feuille = 2
Ciseaux = 3
joueur_score = 0
ordinateur_score = 0

names = {Pierre: "Pierre", Feuille: "Feuille", Ciseaux: "Ciseaux"}
rules = {Pierre: Ciseaux, Feuille: Pierre, Ciseaux: Feuille}


print "Pierre, feuille, ciseaux"
print " "
print "1. PC vs Humain"
print "2. Humain vs Humain"
print " "
print "\n1 ou 2 ?"
rep = raw_input ( " ")
rep = int(rep)
if rep == 1:

        def start():
                print "C'est partie pour pierre, feuille, ciseaux"
                while game():
                        pass
                score()

        def game():
                joueur = move()
                ordinateur = random.randint(1, 3)
                result (joueur, ordinateur)
                return recommencer()

        def move():
                while True:
                        print("C'est partie !")
                        print " "
                        print "1. Pierre"
                        print "2. Feuille"
                        print "3. Ciseaux"
                        print " "
                        print ("\nVotre choix entre 1, 2 et 3")
                        joueur = raw_input(" ")
                        try:
                                joueur = int(joueur)
                                if joueur in (1, 2, 3):
                                        return joueur
                        except ValueError:
                                pass
                        print "Vous devez choisir entre 1, 2 et 3"

        def result(joueur, ordinateur):
                print "Ordinateur a pris {0}".format(names[ordinateur])
                global joueur_score, ordinateur_score
                print " "
                if joueur == ordinateur:
                        print "Egaliter !"
                else :
                        if rules[joueur] == ordinateur:
                                print "Tu as gagne !"
                                joueur_score += 1
                        else :
                                print "Tu as perdu !"
                                ordinateur_score += 1

        def recommencer():
                reponse = raw_input("Recommencer ? y/n: ")
                if reponse.lower() in ["y", "yes", "oui", "o"]:
                        return reponse
                else:
                        print "Bye !"

        def score():
                global joueur_score, ordinateur_score
                print "Les scores :"
                print "Joueur", joueur_score
                print "Ordinateur", ordinateur_score


if rep == 2:

        joueur_score = 0
        joueur_deux_score = 0
        import os

        names = {Pierre: "Pierre", Feuille: "Feuille", Ciseaux: "Ciseaux"}
        rules = {Pierre: Ciseaux, Feuille: Pierre, Ciseaux: Feuille}

        def start():
                print "C'est partie pour pierre, feuille, ciseaux"
                while game():
                        pass
                score()

        def game():
                while True:
                        print("C'est partie premier joueur !")
                        print " "
                        print "1. Pierre"
                        print "2. Feuille"
                        print "3. Ciseaux"
                        print " "
                        print ("\nVotre choix entre 1, 2 et 3")
                        joueur = raw_input(" ")
                        os.system('clear')
                        try:
                                joueur = int(joueur)
                                if joueur in (1, 2, 3):
                                        return joueur
                        except ValueError:
                                pass
                        print "Vous devez choisir entre 1, 2 et 3"
        def game2():
                os.system('clear')
                joueur_deux = move2()
                result (joueur, joueur_deux)
                return recommencer()

        def move2():
                while True:
                        print("C'est partie deuxieme joueur !")
                        print " "
                        print "1. Pierre"
                        print "2. Feuille"
                        print "3. Ciseaux"
                        print " "
                        print ("\nVotre choix entre 1, 2 et 3")
                        joueur_deux = raw_input(" ")
                        try:
                                joueur_deux = int(joueur_deux)
                                if joueur_deux in (1, 2, 3):
                                        return joueur_deux
                        except ValueError:
                                pass
                        print "Vous devez choisir entre 1, 2 et 3"

        def result(joueur, joueur_deux):
                print "Ordinateur a pris {0}".format(names[joueur_deux])
                global joueur_score, joueur_deux_score
                print " "
                if joueur == joueur_deux:
                        print "Egaliter !"
                else :
                        if rules[joueur] == joueur_deux:
                                print "Joueur 1 gagne !"
                                joueur_score += 1
                        else :
                                print "joueur 2 gagne !"
                                joueur_deux_score += 1

        def recommencer():
                reponse = raw_input("Recommencer ? y/n: ")
                if reponse.lower() in ["y", "yes", "oui", "o"]:
                        return reponse
                else:
                        print "Bye !"

        def score():
                global joueur_score, joueur_deux_score
                print "Les scores :"
                print "Joueur 1 ", joueur_score
                print "Joueur 2 ", joueur_deux_score

if __name__ == '__main__':
        start()
