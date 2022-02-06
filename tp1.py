import string


def affiche(S):
    print(S)
    
def to_miniscule(S):
    return S.lower()

def del_space(S):
    return S.replace(' ','')

def saisire(T= 'Entrez une donnee : '):
    S =  raw_input(T)
    return S

def get_indice(x):
   tab = list(string.ascii_lowercase)
   if x in tab:
       return tab.index(x)
   print("Erreur au niveau de get_indice. Elle retourne -1")
   return -1

def get_lettre(i):
   tab = list(string.ascii_lowercase)
   if i <= len(tab) and i >= 0:
    return tab[i]
   else:
       return ''   


def local_crypt(Ti,Ci):
    return get_indice(Ti) + get_indice(Ci)

def local_decrypt(Ti,Ci):
    return get_indice(Ti) - get_indice(Ci)



def crypt(x,c):
    final_text = ''

    for i in range(0,len(x)):
        final_text += get_lettre(local_crypt(x[i],c[i%len(c)])%26)

    return final_text



def decrypt(x,c):
    final_text = ''

    for i in range(0,len(x)):
        final_text += get_lettre(local_decrypt(x[i],c[i%len(c)])%26)

    return final_text



def interface_cryptage():
    x = str(saisire())    # 'CHIFFRE DE VIGENERE'
    c = str(saisire("Entrez une cle: ")) # "BACHELIER"
    

    print("------------------BASE---------------------------")
    print("Phrase de base: "+x)
    print("Cle de base: "+c)

    x = del_space(to_miniscule(x)) 
    c = del_space(to_miniscule(c))  

    print("--------------TRANSFORMATION---------------------")
    print("Phrase: "+x)
    print("Cle: "+c)
    xCri = crypt(x,c)
    print("--------------CHIFFREMENT------------------------")
    print("Phrase: "+xCri)
    xDec = decrypt(xCri,c)
    print("--------------DE-CHIFFREMENT---------------------")
    print("Phrase: "+xDec)
   
#x = 'CHIFFRE DE VIGENERE'
#c = "BACHELIER"
#x = del_space(to_miniscule(x)) 
#c = del_space(to_miniscule(c))
#interface_cryptage()
