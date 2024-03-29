import os
import sys

# add local modules to the module path
this_file = os.path.abspath(__file__)
module_dir = os.path.normpath(os.path.join(os.path.dirname(this_file), ".."))
sys.path.insert(0, module_dir)

from AssocMining import HashSet
from AssocMining.Apriori import prune, exec_apriori

if __name__ == '__main__':
    minsupport = 3
    hs = HashSet()

    file = open("example.txt")
    C1 = hs.fromRaw(file)
    file.close()

    L1 = prune(C1, minsupport)

    Ck = exec_apriori(L1)
    print("====================================")
    print("Frequent 1 - itemset is", [elem['set'] for elem in L1.dictArray])
    print("====================================")
    k=2
    while Ck is not None and Ck.dictArray:
        Lk = prune(Ck, minsupport)

        print("====================================")
        print("Frequent",k,"- itemset is", [elem['set'] for elem in Lk.dictArray])
        print("====================================")

        k += 1
        Ck = exec_apriori(Lk)


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
