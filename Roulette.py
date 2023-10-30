
import random
import pickle


Nb_machine = random.randrange(0, 100)
chans = 5
score_user = 0

try:
    
    with open('Db.pkl', 'rb') as f:
        Db= pickle.load(f)
except (FileNotFoundError, EOFError):
    
    Db = {}
    while True:
        pseudo = input("Entrez votre pseudo : ")
        if not pseudo.islower():
            print("Le pseudonyme doit être en minuscules.")
        elif ' ' in pseudo:
            print("Le pseudonyme ne doit pas contenir d'espaces.")
        else:
            break

    if pseudo not in Db:
        Db[pseudo] = {}

    with open('database.pkl', 'wb') as f:
        pickle.dump(Db, f)

    print("Pseudonyme ajouté à la base de données.")
    
while True:
    while chans > 0:
        User = int(input("Entrez un nombre : "))

        if 0 <= User <= 100:
            if Nb_machine == User:
                score_user += chans * 30 
                print("Bravo !", pseudo, "vous avez gagné!")
                print("Votre score est maintenant de", score_user)
                break
            else:
                print("Dommage !", pseudo, "vous avez perdu")
                chans -= 1
                print("Il vous reste:",chans, "chances") 
        else:
            print("Le nombre doit être compris entre 0 et 100.")

    if chans == 0:
        print("Vous n'avez plus de chances restantes. Le nombre était", Nb_machine)

    
    print("Partie terminée")
    print(pseudo, ';', score_user)
    
    kanpe = input("Presser K pour arreter le programme")
    if kanpe.lower()=='k':
            chans==0
            print("merci d'avoir participer")
            exit()
    else:
        chans=5
        Nb_machine = random.randrange(0, 100)
        print("vous avez  {} de la chance de jouer avec nou".format(chans))
            
        
