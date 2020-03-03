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
        self.dictArray = list(dict())
        self.fstr = None


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

        return flag

    def add(self, setDict):
        self.dictArray.append({'set': set(setDict['set']), 'count': setDict['count']})

    def fromFile(self, fstr):
        self.fstr = fstr
        file = open(fstr)

        for line in file:
            for item in map(str.strip, line.split(',')):
                if self.check_set_exists(set(item)):
                    self.dictArray[self.get_set_index(set(item))]['count'] += 1
                else:
                    self.add({'set': set(item), 'count': 1})

        file.close()

        return self.dictArray

    def reHash(self):
        file = open(self.fstr)

        for element in self.dictArray:
            for item in map(str.strip, line.split(',')):
                if self.check_set_exists(set(item)):
                    self.dictArray[self.get_set_index(set(item))]['count'] += 1
                else:
                    self.add({'set': set(item), 'count': 1})

        file.close()

    # if __name__ == '__main__':
