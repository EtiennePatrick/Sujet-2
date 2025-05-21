import hashlib
import sys

def hasher(mot, algo):
    mot = mot.strip()
    if algo == "md5":
        return hashlib.md5(mot.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(mot.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(mot.encode()).hexdigest()
    else:
        print("[-] Algorithme non supporté.")
        sys.exit(1)

def crack(dictionnaire, hash_cible, algo):
    with open(dictionnaire, "r") as f:
        for ligne in f:
            mot = ligne.strip()
            hash_mot = hasher(mot, algo)
            if hash_mot == hash_cible:
                print(f"[+] Mot de passe trouvé : {mot}")
                return
    print("[-] Mot de passe non trouvé dans le dictionnaire.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Utilisation : python crackage_hash.py <dictionnaire.txt> <hash> <algo>")
        print("Exemple : python crackage_hash.py dictionnaire.txt e10adc3949ba59abbe56e057f20f883e md5")
        sys.exit(1)

    dictionnaire = sys.argv[1]
    hash_cible = sys.argv[2]
    algo = sys.argv[3].lower()

    crack(dictionnaire, hash_cible, algo)
