class Solution:
    def countCharacters(self, s: str):
        Dict = {}
        for i in range(len(s)):
            if s[i] not in Dict.keys():
                Dict[s[i]] = 1
            else:
                Dict[s[i]] += 1
            
        print(Dict)
        
if __name__ == '__main__':
    test = Solution
    testString = '''The new patients were an 18-year-old female student who returned from Britain on Friday,
                    and a 61-year-old man whose granddaughter and domestic helper was infected previously,
                    according to Dr Chuang Shuk-kwan, head of the Centre for Health Protection’s
                    communicable disease branch.'''
    result = test.countCharacters(Solution(), testString)
