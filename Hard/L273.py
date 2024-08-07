class Solution:
    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                    "Eighteen", "Nineteen"]
    TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return Solution.LESS_THAN_20[num] + " "
            elif num < 100:
                return Solution.TENS[num // 10] + " " + helper(num % 10)
            else:
                return Solution.LESS_THAN_20[num // 100] + " Hundred " + helper(num % 100)

        words = []
        for i in range(len(Solution.THOUSANDS)):
            if num % 1000 != 0:
                words.append(helper(num % 1000) + Solution.THOUSANDS[i])
            num //= 1000

        return ' '.join(reversed(words)).strip()
