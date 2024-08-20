class Solution:
    def stoneGameVI(self, aliceValues: list[int], bobValues: list[int]) -> int:
        hp = [(-(aliceValues[i] + bobValues[i]), aliceValues[i], bobValues[i]) for i in range(len(aliceValues))]
        heapq.heapify(hp)

        alice_turn = True
        alice_score = 0
        bob_score = 0

        while hp:
            _, alice_value, bob_value = heapq.heappop(hp)
            if alice_turn:
                alice_score += alice_value
            else:
                bob_score += bob_value
            alice_turn = not alice_turn

        # Compare Alice's and Bob's final scores
        return (alice_score > bob_score) - (alice_score < bob_score)
