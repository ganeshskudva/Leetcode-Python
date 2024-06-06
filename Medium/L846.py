class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        mp = collections.Counter(hand)
        hp = list(mp.keys())
        heapq.heapify(hp)
        while len(hp):
            num, start = mp[hp[0]], heapq.heappop(hp)
            if num:
                for i in range(1, groupSize):
                    if (start + i) not in mp or mp[start + i] < num:
                        return False
                    else:
                        mp[start + i] -= num

        return True
