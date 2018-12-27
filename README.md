# methode-de-cesar
##METHODE DE CESAR
mot=input("Entrez le message: ")
y=input("Entrez un decallage: ")
y=int(y)
#Définition de la fonction décallage avec y=décallage choisit
def decallage(mot,y):
    T = ""
    #On parcours chaque lettre du mot
    for lettre in mot:
       #On transforme la lettre en sa valeur de caractère et on y ajoute le décallage avec ord()
       x=ord(lettre)+y
       #On reconvertit la lettre ( décallée ) en caractère avec chr()
       T += chr(x)
    return(T)
print(decallage(mot,y))
#On demande à l'utilisateur de saisir le message qu'il souhaite décrypter
MessageCrypte=input("Entrez le message crypté: ")
#On parcours chaque lettre du message crypté
lettr=len(MessageCrypte)
#On met le futur message décrypté en chaine de caractère
MessageClair=""
#On demande à l'utilisateur de saisir un décallage
decal=input("Entrer le décallage jusqu'a trouver le bon :): ")
decal=int(decal)
#On rentre dans une boucle for pour parcourir tous les indices des lettres
for i in range(lettr):
    if MessageCrypte[i]==' ':
        MessageClair+=' '
    else:
        #On transforme les lettres du message crypté en leur valeur de caractère avec ord()
        asc=ord(MessageCrypte[i])-decal
        #On reconvertit les lettres (décallées) en caractère avec chr()
        MessageClair+=chr(asc+26*((asc<65)-(asc>90)))
#On affiche le message qui est peut-être décrypté si le décallage est le bon
print (MessageClair)
#On demande à l'utilisateur si le message est bien décrypté
convient=input("Est ce le bon décallage?: 1 - oui/ 2 - non : ")
convient=int(convient)
#S'il est bon alors l'utilisateur choisit 1 et on affiche un message qui félicite l'utilisateur
if(convient==1):
    print("BRAVO ! Vous avez decrypté le code!")
#S'il n'est pas bon alors l'utilisateur saisit 2 et le processus d'avant recommencent
#jusqu'à ce que l'utilisateur trouve le bon décallage
while(convient==2):
    MessageCrypte=input("Entrez le message crypté: ")
    lettr=len(MessageCrypte)
    MessageClair=""
    decal=input("Entrer le décallage jusqu'a trouver le bon :): ")
    decal=int(decal)

    for i in range(lettr):
        if MessageCrypte[i]==' ':
            MessageClair+=' '
        else:
            asc=ord(MessageCrypte[i])-decal
            MessageClair+=chr(asc+26*((asc<65)-(asc>90)))
    print (MessageClair)
    convient=input("Est ce le bon décallage?: 1 - oui/ 2 - non : ")
    convient=int(convient)
    if(convient==1):
        print("BRAVO ! Vous avez decrypté le code!")
