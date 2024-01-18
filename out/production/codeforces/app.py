str_a_chercher = input("Enter a string: ")

length_string = len(str_a_chercher)

result = ""

character_tester = ""

counter = 1

for i in range(length_string):
    result += '*'
    
while True:
    if counter != 10:
        print("Tentative : {}".format(counter))
        print("Caractères testés : {}".format(character_tester))
        # Récupération du charactère
        character = input("Saissisez un caractère: ")
        # Si le charactère est dans la chaine de caractère
        if character in str_a_chercher:
            # On récupère tous les indexs où le charactère est présent
            indexs = [i for i, x in enumerate(str_a_chercher) if x == character]
            #  Pour chaque index on ajoute le charactère à la chaine de caractère result
            result = result[:indexs[0]] + character + result[indexs[0]+1:]
            # Test si on est à la fin du jeu cad que result = input 
            if result.lower() == str_a_chercher.lower():
                print("Vous avez gagné ! <3")
                print("Le mot était : " + str_a_chercher)
                break
            print("Mot courant : " + result)
            character_tester += character + ","
            counter += 1
        else :
            print("Le caractère n'est pas dans la chaine de caractère.")
            character_tester += character + ","
            # On recommence la boucle
            counter += 1
            continue
    else:
        print("Vous avez perdu :(")
        print("Le mot était : " + str_a_chercher)
        # On sort de la boucle et termine le jeu
        break