"""
 Ce fichier va permettre de vérifier si le mot est un palindrome
"""
#### Fonction secondaire

def ispalindrome(s):
    """
    Cette fonction va permettre de vérifier si le mot 
    peut se lire indifféremment de gauche à droite 
    ou de droite à gauche en gardant le même sens

    >>> ispalindrome("non")
    True

    """
    # creer une table pour retirer tous les caractères non désirable
    table = str.maketrans("éèàêôëç", "eeaeoec", "\t\n,?!:- '")
    # applique la table
    s=s.lower()
    s=s.translate(table)
    if s[::-1] == s:
        return True
    return False

#### Fonction principale


def main():
    """
    Ici on vient faire l'appel de la fonction 
    """
    print(ispalindrome("bonjour"))
    print(ispalindrome("laval"))
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
