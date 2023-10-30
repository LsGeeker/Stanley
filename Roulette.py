import random
import pickle

Nb_machine = random.randrange(0, 100)
chans = 5
age = 18
score_user = 0
Nb_user = 0

try:
    
    with open('database.pkl', 'rb') as f:
        database = pickle.load(f)
except (FileNotFoundError, EOFError):
    
    database = {}

while True:
    
    while True:
        pseudo = input("Entrez votre pseudo : ")

        
        if not pseudo.islower():
            print("Le pseudonyme doit être en minuscules.")
        elif ' ' in pseudo:
            print("Le pseudonyme ne doit pas contenir d'espaces.")
        
        else:
            break  

    age = int(input("Quel est votre âge : "))
    database[pseudo] = {'age': age}

    if age >= 18:
        print("Vous êtes matures, vous pouvez continuer.")
    else:
        print("Jeux interdit aux moins de 18 ans.")
        exit()

    with open('database.pkl', 'wb') as f:
        pickle.dump(database, f)

    print("Pseudonyme ajouté à la base de données.")

    while chans > 0:
        User = int(input("Entrez un nombre  de 0 a 100 : ")) 

        if Nb_machine == User:
            score_user += 10 
            print("Bravo !", pseudo, "vous avez gagné!")
            print("Votre score est maintenant de", score_user)
            break
        else:
            print("Dommage !", pseudo, "vous avez perdu")
            score_user =0
            chans -= 1
           

    if chans == 0:
        print("Vous n'avez plus de chances restantes. Le nombre était", Nb_machine)
        break
    


