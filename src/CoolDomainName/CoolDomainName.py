class CoolDomainName:
    alphabet = {
        'a': ['4', '5'],
        'e': ['3'],
        'i': ['1'],
        'l': ['1'],
        'o': ['0'],
        'u': [],
    }

    def isDomainNameCool(self, name, domain):
        name = name.lower()
        namesTosearch = self.leetName(domain)
        for nameToSearch in namesTosearch:
            if nameToSearch in name:
                return True
        return False

    def leetName(self, name):
        ret = []
        for i in range(0, self.countIterations(name)):
            ret.append(self.leetIterate(name, i))
        return ret

    def countIterations(self, name):

        ret = 1
        alphabet = self.getAlphabet()
        for letter in name:
            if letter in alphabet:
                ret *= len(self.getCylinder(letter))
        return ret

    def getAlphabet(self):
        _ret = self.alphabet
        for letter in _ret:
            if not letter in _ret[letter]:
               _ret[letter].append(letter)
        return _ret

    def getCylinder(self, letter):
        alphabet = self.getAlphabet()
        cylinder = self.arPosition(alphabet, letter)
        if(cylinder == -1):
            cylinder = [letter]
        return cylinder

    def leetIterate(self, word, iteration):
        ret = ''
        positions = self.itos(word, iteration)
        for i in range(0, len(word)):
            if i >= len(positions):
                positions.append(0)
            ret += self.getCylinder(word[i])[positions[i]]
        return ret

    def arPosition(self, array, position):
        for x in array:
            if position == x:
                return array[x]
        return -1

    def itos(self, word, num):
        maxc  = self.getMax(word)
        res = []
        index = 0
        while num != 0:
            remainder  = num % maxc[index]
            num        = num / maxc[index]
            res.append(remainder)
            index += 1
        return res

    def getMax(self, word):
        _ret = []
        for letter in word:
            _ret.append(len(self.getCylinder(letter)))
        return _ret
