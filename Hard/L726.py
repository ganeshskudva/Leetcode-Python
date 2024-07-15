class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [1]
        number = ''
        element = ''
        counter = Counter()
        for i in reversed(range(len(formula))):
            if formula[i].isdigit():
                number = formula[i] + number
            elif formula[i] == ')':
                if number:
                    stack.append(int(number) * stack[-1])
                else:
                    stack.append(1)
                number = ''
            elif formula[i] == '(':
                stack.pop()
                number = ''
            elif formula[i].isalpha():
                element = formula[i] + element
                if formula[i].isupper():
                    if number:
                        counter[element] += stack[-1] * int(number)
                    else:
                        counter[element] += stack[-1]
                    element = ''
                    number = ''
        return ''.join([element + (str(counter[element]) if counter[element] > 1 else '') for element in sorted(counter)])
