class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


        for start_index in range(len(gas)):
            tank = 0
            moved = 0
            stopped = False

            for i in range(len(gas)):
                curr_pos = (start_index + i) % len(gas)
                tank += gas[curr_pos]
                gas_needed = cost[curr_pos]

                if gas_needed > tank:
                    stopped = True
                    break;

                tank -= gas_needed

            if not stopped:
                return start_index
        return -1