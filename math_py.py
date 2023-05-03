def est_premier(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def est_entier_relatif(n):
    if n == int(n):
        return True
    else:
        return False

while True:
    print("Choisissez une opération:")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Calculer le PGCD")
    print("6. Vérifier si un nombre est premier")
    print("7. Vérifier si un nombre est un entier relatif")

    choix = input("Entrez votre choix (1/2/3/4/5/6/7): ")

    if choix == '6':
        num = int(input("Entrez un nombre: "))
        if est_premier(num):
            print(num, "est un nombre premier")
        else:
            print(num, "n'est pas un nombre premier")

    elif choix == '7':
        num = float(input("Entrez un nombre: "))
        if est_entier_relatif(num):
            print(num, "est un entier relatif")
        else:
            print(num, "n'est pas un entier relatif")

    elif choix in ('1', '2', '3', '4', '5'):
        num1 = int(input("Entrez le premier nombre: "))
        num2 = int(input("Entrez le deuxième nombre: "))

        if choix == '1':
            print(num1, "+", num2, "=", (num1 + num2))

        elif choix == '2':
            print(num1, "-", num2, "=", (num1 - num2))

        elif choix == '3':
            print(num1, "*", num2, "=", (num1 * num2))

        elif choix == '4':
            if num2 == 0:
                print("Division par zéro impossible")
            else:
                print(num1, "/", num2, "=", (num1 / num2))

        elif choix == '5':
            print("Le PGCD de", num1, "et", num2, "est", pgcd(num1, num2))

        else:
            print("Opération invalide")

    else:
        print("Opération invalide")
