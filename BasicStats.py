class BasicStats:

    @staticmethod
    def createFreqMap(aList):
        dictionary = {}
        for x in aList:
            x.lower()
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1

        return dictionary

    def topN(self, dictionary, num):
        output = {}
        for x in range(num):
            values = list(dictionary.values())
            keys = list(dictionary.keys())
            maximum = max(values)
            index = values.index(maximum)
            key = keys[index]
            output[key] = maximum
            dictionary.pop(key)

        return output

    def bottomN(self, dictionary, num):
        output = {}
        for x in range(num):
            values = list(dictionary.values())
            keys = list(dictionary.keys())
            minimum = min(values)
            index = values.index(minimum)
            key = keys[index]
            output[key] = minimum
            dictionary.pop(key)

        return output
