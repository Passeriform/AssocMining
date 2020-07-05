class HashSet:
    """
    [
        {
            set: { <str> } <set>
            count: <int>
        },
        {
            set: { <str> } <set>
            count: <int>
        },
        ...
    ]
    """
    def __init__(self):
        self.rawSrc = list()
        self.dictArray = list(dict())


    def __iter__(self):
        return (x for x in list.__iter__(self.dictArray) if x is not None)


    def check_set_exists(self, in_set):
        flag = False

        for item in self.dictArray:
            if in_set == item['set']:
                flag = True

        return flag


    def is_empty(self):
        return not self.dictArray


    def get_set_index(self, in_set):
        for idx, item in enumerate(self.dictArray):
            if in_set == item['set']:
                return idx


    def add(self, setDict):
        self.dictArray.append({'set': set(setDict['set']), 'count': setDict['count']})


    def next(self, hashSet):
        hashSet.rawSrc = self.rawSrc;
        return hashSet


    def fromRaw(self, strArr):
        for line in strArr:
            collector = set()
            for item in map(str.strip, line.split(',')):
                collector = collector.union(item)
                if self.check_set_exists(set(item)):
                    self.dictArray[self.get_set_index(set(item))]['count'] += 1
                else:
                    self.add({'set': set(item), 'count': 1})
            self.rawSrc.append(collector)

        return self


    def reHash(self):
        for idx, item in enumerate(self.dictArray):
            for testset in self.rawSrc:
                if set(item['set']).issubset(testset):
                    self.dictArray[idx]['count'] += 1

        return self
