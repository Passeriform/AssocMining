from ..HashSet import HashSet

def exec_apriori(l_hashSet):
    k_hashSet = HashSet()

    for i, dictSetx in enumerate(l_hashSet):
        for j, dictSety in enumerate(l_hashSet):
            if i != j:
                unionset = dictSetx['set'].union(dictSety['set'])
                if k_hashSet.check_set_exists(unionset) is False:
                    k_hashSet.add({'set': unionset, 'count': 0})

    return l_hashSet.next(k_hashSet).reHash()


def prune(c_k_hashSet, min_support):
    L = HashSet()

    for setDict in c_k_hashSet:
        if setDict['count'] >= min_support:
            L.add(setDict)

    return c_k_hashSet.next(L)
