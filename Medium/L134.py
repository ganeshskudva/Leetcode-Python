class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sumGas, sumCost, start, tank = 0, 0, 0, 0
        
        for i in range(len(gas)):
            sumGas += gas[i]
            sumCost += cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                start, tank = i + 1, 0
        
        return -1 if sumGas < sumCost else start
