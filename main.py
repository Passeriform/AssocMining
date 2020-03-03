#!/usr/bin/env python

from AssocMining import HashSet
from AssocMining.Apriori import prune, exec_apriori

if __name__ == '__main__':
    minsupport = 3
    hs = HashSet()

    C1 = hs.fromFile("example.txt")

    L1 = prune(C1, minsupport)

    Ck = exec_apriori(L1)
    print("====================================")
    print("Frequent 1-itemset is", [elem['set'] for elem in L1.dictArray])
    print("====================================")
    k=2
    while Ck.is_empty() is False:

        print(Ck.dictArray)
        Lk = prune(Ck, minsupport)

        print("====================================")
        print("Frequent",k,"-itemset is", [elem['set'] for elem in Lk.dictArray])
        print("====================================")
        Ck = exec_apriori(Lk)
        k += 1



"""
====================================
Frequent 1-itemset is ['a', 'b', 'c', 'f', 'm', 'p']
====================================
====================================
Frequent 2 -itemset is ['ac', 'af', 'am', 'cf', 'cm', 'cp', 'fm']
====================================
====================================
Frequent 3 -itemset is ['acf', 'acm', 'afm', 'cfm']
====================================
====================================
Frequent 4 -itemset is ['acfm']
====================================
"""
