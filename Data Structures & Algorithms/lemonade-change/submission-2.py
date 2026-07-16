class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        till = {5: 0, 10:0, 20: 0}

        for bill in bills:
            till[bill] += 1

            change_required = bill - 5

            if change_required == 5:
                if till[5] < 1:
                    return False
                elif till[5]  >= 1:
                    till[5] -= 1

            if change_required == 10:
                if till[5] < 2 and till[10] < 1:
                    return False
                elif till[10] >= 1:
                    till[10] -= 1
                else: 
                    till[5] -= 2

            if change_required == 15:
                print("hello")
                if till[10] >= 1 and till[5] >= 1:
                    till[10] -= 1
                    till[5] -= 1
                elif till[5] >= 3: 
                    till[5] -= 3
                else:
                    return False

            print(till)


        return True