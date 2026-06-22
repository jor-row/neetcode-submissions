class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert each string to a dictionary
        # then have a dictionary with the key a dictionary and 
        # value an array of all words that match that dictionary

        def convertToDict(s: str) -> dict:
            sCount = {}

            for a in s:
                if a in sCount.keys():
                    sCount[a] += 1
                else:
                    sCount[a] = 1
            
            return sCount

        counts = []

        for s in strs:
            sCount = convertToDict(s)

            if len(counts) == 0:
                counts.append([s])
            else:
                foundAna = False
                for count in counts:
                    if convertToDict(count[0]) == sCount:
                        count.append(s)
                        foundAna = True
                        break
                
                if foundAna == False:
                    counts.append([s])
        
        return counts





        