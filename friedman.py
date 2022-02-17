from vig_analyse import *
# indice de coincidence dans un texte anglais
Ke = 0.067

# indice de coincidence dans un texte aleatoire
Kr = 0.0385


# In: texte T
# Out: float ,indice de coincidence de T
def indice_coincidence(T):
    T = clean_string(T)
    n = len(T)
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    D = dict()
    for c in Alphabet:
        D[c] = 0

    for c in T:
        if c in D.keys():
            D[c] +=1

    ic = 0
    for k in D.keys():
        ic += D[k] * (D[k]-1)
    print
    return float(ic)/float(n*(n-1))


def approximate_size_key_friedman(T):
    T = clean_string(T)
    K = indice_coincidence(T)
    return((Ke-Kr)/(K-Kr))

