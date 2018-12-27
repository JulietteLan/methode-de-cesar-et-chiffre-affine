#Initialisation, entrée du mot et du décallage
mot=input("Entrez le message: ")
y=input("Entrez un decallage: ")
y=int(y)
#Fonction qui convertit les lettres en leur valeur
def num(caractere):
    return ord(caractere)-65
#Fonction pour décaller les valeurs
def decallage(y):
    return chr(y+65)
#Boucle for pour parcourir chaque lettre et les décaller
for lettre in mot:
    c=(num(lettre)*11+7)%26
    print(c)

