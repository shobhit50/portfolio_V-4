class Solution:
    def encode(self, strs):
        neww = ''

        for st in strs:
            neww +=  str(len(st)) + '#' + st

        s = self.decode(neww)
        print('Decode str =', s)
        return strs
    
    def decode(self, s):
        newList = list()
        newstr = ''
        count = 0

        for i in range(len(s)):
            if s[i].isdigit():
                count = count * 10 + int(s[i])
            elif s[i] == '#':
                for j in range(i + 1, i + 1 + count):
                    newstr += s[j]
                newList.append(newstr)
                newstr = ''
                count = 0

        return newList

incode = ['neet', 'code', 'neetcode']
Solution().encode(incode)