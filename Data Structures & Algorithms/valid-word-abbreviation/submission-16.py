class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        count = 0
        currNum = ""

        print(len(word))

        if word == abbr:
            return True

        for s in abbr:
            if s.isalpha():
                count += 1
                if currNum != "":
                    print("adding, ", currNum)
                    count += int(currNum)
                    currNum = ""

                if count > len(word) or s != word[count - 1]:
                    return False
            elif s.isnumeric():
                if currNum == "" and s == "0":
                    return False
                currNum += s

        if currNum != "":
            count += int(currNum)
            currNum = ""

        return count == len(word)
        