from ..HashSet import HashSet

def exec_apriori(l_hashSet):
    k_hashSet = HashSet()

    for i, dictSetx in enumerate(l_hashSet):
        for j, dictSety in enumerate(l_hashSet):
            if i != j:
                unionset = dictSetx['set'].union(dictSety['set'])
                if k_hashSet.check_set_exists(unionset) is False:
                    k_hashSet.add({'set': unionset, 'count': 0})

    return k_hashSet


def prune(c_k_hashSet, min_support):
    L = HashSet()

    for setDict in c_k_hashSet:
        if setDict['count'] >= min_support:
            L.add(setDict)

    return L


def check_set_exists(candidate):
    """ Use bool to know is subset or not """
    Lk = dict()
    file = open("example.txt")
    for l in file:
        l = str(l.split())
        count = 0
        for i in range (0,len(candidate)):
            key = str(candidate[i])
            if key not in Lk:
                Lk[key] = 0
            flag = True
            for k in key:
                if k not in l:
                    flag = False
            if flag:
                Lk[key] += 1
    file.close()
    return Lk
