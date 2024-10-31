from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        # Initialize a list to keep track of visited accounts
        # Space Complexity: O(n), where n is the number of accounts
        visited_accounts = [False] * len(accounts)
        
        # `emails_accounts_map` maps each email to a list of account indices that contain it
        # Space Complexity: O(e + n), where e is the total number of emails and n is the number of accounts
        emails_accounts_map = defaultdict(list)
        
        # Result list to store the merged account information
        # Space Complexity: O(n + e), since we may store each email and account name
        res = []

        # Step 1: Build the graph where each email points to account indices containing that email
        # Time Complexity: O(n * k), where n is the number of accounts and k is the average number of emails per account
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):  # Start from 1 to skip the account name
                email = account[j]
                emails_accounts_map[email].append(i)

        # Step 2: Define a DFS function to traverse accounts and gather emails for each connected component
        # Time Complexity of `dfs`: O(n * k), as each email and account is processed once
        def dfs(i, emails):
            # If this account has already been visited, return to avoid re-processing
            if visited_accounts[i]:
                return
            # Mark the account as visited
            visited_accounts[i] = True
            # Traverse all emails associated with this account
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)  # Collect the email
                # Visit all neighboring accounts that share this email
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)

        # Step 3: Perform DFS on each unvisited account and collect merged account data
        # Time Complexity: O(n * k log k), where sorting the emails takes O(k log k) for each component
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()  # Initialize account name and a set for emails
            dfs(i, emails)  # Perform DFS to gather all connected emails for the account
            # Append the account name and sorted list of emails to the result
            res.append([name] + sorted(emails))

        # Return the merged accounts
        return res

# Overall Complexity Summary:
# Time Complexity: O(n * k log k), where n is the number of accounts and k is the average number of emails per account.
#   - Building the graph (adjacency list) takes O(n * k).
#   - DFS traversal takes O(n * k) since we visit each account and email once.
#   - Sorting each account’s emails takes O(k log k), and we sort for each component.
# Space Complexity: O(n * k), for storing the graph, visited list, and the result.
#   - `visited_accounts` requires O(n) space.
#   - `emails_accounts_map` requires O(e + n) space, where e is the number of unique emails.
#   - `res` requires O(n + e), storing merged accounts with unique emails.
