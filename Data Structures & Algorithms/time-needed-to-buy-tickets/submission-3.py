class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        foqi = 0
        secs = 0

        while tickets[k] > 0:

            if tickets[foqi] == 0:
                foqi  = (foqi+1) % len(tickets)
            else:
                tickets[foqi] -= 1
                secs += 1
                foqi  = (foqi+1) % len(tickets)


        return secs


        