from vig import *


# In: texte 
# Out: dict avec chaque occurence pour chaque sous-mot
def get_occurences(texte):
    dictionnaire = dict()
    for i in range(0,len(texte)):
        
        for j in range(i,len(texte)+1):
            dictionnaire[texte[i:j]] = dict()
            dictionnaire[texte[i:j]]['count'] = 0 

    for k in dictionnaire.keys():
        dictionnaire[k]['count'] =  texte.count(k)
        dictionnaire[k]['dist'] =  -1
        dictionnaire[k]['pos'] = [] 
    del dictionnaire['']

    return dictionnaire


#In: string and word
# Out : list with all positions of this word in the string 
def position(word,string):
    positionTemp = [] 
    position = [] 
    for i in range(0,len(string)):
        if word in string[i:]:
            index = string[i:].index(word)
            positionTemp.append(index+i)
         
    for i in positionTemp:
        if i not in position:
            position.append(i)
    return position


            
# In: dict
# Out: dict without occurences single appearance and len(occ) >= 3
def clean_Occ(occurences):
    Cocc = dict()
    for k in occurences.keys():
        if occurences[k]['count'] > 1 and len(k) >= 3:
            Cocc[k] =  occurences[k]
    return Cocc


# In: dict
# Out: dict without occurences with differents distances (-1)
"""def clean_Occ_dist(occurences):
    Cocc = dict()
    for k in occurences.keys():
        if occurences[k]['dist'] ==  -1:
            Cocc[k] =  occurences[k]
    return Cocc
"""
# In: dict
# Out: dict with out differents distances
def clean_distance_tab(D):
    D2 = dict()
    for k in D.keys():
        if len( D[k]['dist'] ) == 1:
            D2[k] = D[k]
            D2[k]['dist'] =  D2[k]['dist'][0]

    return D2

# In: number a ,number  b
# Out: number abs(a-b) 
def distance(a,b):
    return abs(int(a) - int(b))

# In: numbers tab 
# Out: distance between all element in the tab 
def distance_tab(tab):
    tempDist = []
    for p1 in tab:
        for p2 in tab:
            if p1 != p2:
                tempDist.append(distance(p1,p2))
    return tempDist
 
# In: dict,string
# Out: dict with distance between 2 occurences
def comupte_distance(string,D):
    for k in D.keys():
       finalDist =[] 
       D[k]['pos'] = position(k,string) 
       tempDist = distance_tab( D[k]['pos'] )
      # print(k,tempDist)
       for i in tempDist:
           if i not in finalDist:
               finalDist.append(i)

       D[k]['dist'] = finalDist


#In: int n
#Out: list of x in [1,n[ where n = k * x ,k integer 
def getFacteurs(n):
    facteurs =[] 
    for i in range(1, n + 1):
        if n % i == 0:
            facteurs.append(i)
    return facteurs

#In: list l1 and list l2
# Out: l1 + l2 list
def concat_list(l1,l2):
    lx = l1
    for e in l2:
        if e not in lx:
            lx.append(e)
    return lx

# In : Dict D
#Out : D with factor of all distances
def facteurs_for_all(D):
    for k in D.keys():
        D[k]['fact']  = []
        for d in D[k]['dist']:
               D[k]['fact'] = concat_list(D[k]['fact'],getFacteurs(d)) 


# In: Dict D
# Out : nothing,but print key with probability
def aproximate_key(D):
    length = len(D.keys())
    stat = dict()
    for k in D.keys():
        for f in D[k]['fact']:  
            if f in stat.keys():
                stat[f] += 1
            else:
                stat[f] = 1
    print('Nombre total d occurences : ',length)
    for k in stat.keys():
        if int(int(stat[k])*100/int(length)) > 10:
            print('Le nombre '+str(k)+' est facteur de '+str(int(stat[k])*100/int(length))+' % des distances entre occurences.')


"""
x = "S'OUVRIT POUR NICOLE UNE PHASE EPUISANTE. L'INCONSCIENT LIGOTAIT PAR L'ORGUEIL SE FENDILLAIT. JAMAIS ELLE N'AVAIT TANT REVE. DES VISAGES DE NOYES AFFLEURAIENT A LA SURFACE D'UNE MER ETALE. ELLE VOYAIT LES YEUX VERTS S'OUVRIR ET SE REFERMER COMME LES VALVES LENTES D'UN COQUILLAGE ENTRE DEUX EAUX. LE SOMMEIL EMPORTAIT CES FACES DE GISANTS."
c = "ROI"
x = clean_string(x)
c = clean_string(c)
#strin = crypt(x,c)#print(strin)


D = "CS AZZMEQM, CO XRWF, CS DZRM GFMJECV. X'IMOQJ JC LB NLFMK CC LBM WCCZBM KFIMSZJSZ CS URQIUOU. CS ZLPIE ECZ RMWWTV, SB KCCJ QMJ FCSOVJ GCI ZI ICCKS, MK QMLL YL'CV ECCJ OKTFWTVM JIZ CO XFWBIWVV, IV ACCI CC C'OCKFM, JINWWB U'OBKSVUFM"
D = clean_string(D)

occ= clean_Occ(get_occurences(D))
comupte_distance(D,occ)
facteurs_for_all(occ)
aproximate_key(occ)
#print(occ)

"""

