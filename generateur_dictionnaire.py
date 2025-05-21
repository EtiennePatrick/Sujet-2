import itertools
import sys

def generer_dictionnaire(longueur_min, longueur_max, caracteres, fichier_sortie="dictionnaire.txt"):
    with open(fichier_sortie, "w") as f:
        for longueur in range(longueur_min, longueur_max + 1):
            for combinaison in itertools.product(caracteres, repeat=longueur):
                mot = ''.join(combinaison)
                f.write(mot + "\n")
    print(f"[+] Dictionnaire généré avec succès dans '{fichier_sortie}'.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Utilisation : python generateur_dictionnaire.py <longueur_min> <longueur_max> <caractères>")
        print("Exemple : python generateur_dictionnaire.py 2 4 abc123")
        sys.exit(1)

    longueur_min = int(sys.argv[1])
    longueur_max = int(sys.argv[2])
    caracteres = sys.argv[3]

    generer_dictionnaire(longueur_min, longueur_max, caracteres)
