import hashlib
import sys

def generer_hash(mot_de_passe, algo):
    if algo == "md5":
        return hashlib.md5(mot_de_passe.encode()).hexdigest()
    elif algo == "sha1":
        return hashlib.sha1(mot_de_passe.encode()).hexdigest()
    elif algo == "sha256":
        return hashlib.sha256(mot_de_passe.encode()).hexdigest()
    else:
        print("[-] Algorithme non supporté. Utilisez : md5, sha1 ou sha256.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python hasher.py <mot_de_passe> <algorithme>")
        print("Exemple : python hasher.py 1234 md5")
        sys.exit(1)

    mot = sys.argv[1]
    algo = sys.argv[2].lower()

    hash_resultat = generer_hash(mot, algo)
    print(f"[+] Hash ({algo}) de '{mot}' : {hash_resultat}")
