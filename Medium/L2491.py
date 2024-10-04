class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # Sort the list of player skills in ascending order to enable pairing
        skill.sort()

        # Calculate the target total skill per pair based on the first and last players
        tot_skill = skill[0] + skill[-1]

        # Initialize a variable to accumulate the total chemistry sum
        chem_sum = 0

        # Iterate over the first half of the sorted skill list
        for i in range(len(skill) // 2):
            # Check if the current pair's combined skill equals the target total skill (tot_skill)
            if skill[i] + skill[-i - 1] != tot_skill:
                # If any pair doesn't match the target skill, return -1 (invalid pairing)
                return -1
            
            # Accumulate chemistry as the product of both players' skills
            chem_sum += skill[i] * skill[-i - 1]

        # Return the total chemistry sum after all pairs have been successfully matched
        return chem_sum
