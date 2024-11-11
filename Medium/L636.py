# Penalty based approach
class Solution:
    def exclusiveTime(self, n, logs):
        # Initialize the result array with zeros, where ans[i] will store
        # the exclusive time for function i
        ans = [0] * n
        
        # Initialize an empty stack to keep track of function call timings.
        # Each element in the stack will be a list [function_id, start_time].
        stack = []
        
        # Loop through each log entry in the logs
        for log in logs:
            # Split the log into function id, event type (start/end), and timestamp
            f_id, event, time = log.split(':')
            f_id, time = int(f_id), int(time)  # Convert function ID and time to integers
            
            if event == 'start':
                # If the event is a "start", push the function ID and start time onto the stack
                stack.append([f_id, time])
            else:
                # If the event is "end", pop the most recent function from the stack
                popped = stack.pop()
                
                # Calculate the exclusive time for the function at the top of the stack
                # and add it to the result for that function. +1 is added because "end" is inclusive.
                ans[popped[0]] += time - popped[1] + 1
                
                # If there's a function still on the stack (i.e., a parent function),
                # subtract the current function's total time from the parent's exclusive time,
                # as it overlaps with the parent's time span.
                if stack:
                    ans[stack[-1][0]] -= time - popped[1] + 1
        
        # Return the final list of exclusive times for each function
        return ans

# Time Complexity (TC): O(L), where L is the number of logs.
# - We iterate through each log exactly once, performing O(1) operations for each log.

# Space Complexity (SC): O(N + L), where:
# - O(N) is for the `ans` array, which stores exclusive time for each of the `n` functions.
# - O(L) is for the `stack`, which, in the worst case, can hold all logs if all are "start" logs consecutively.

# Standard approach
class Solution:
    def exclusiveTime(self, n, logs):
        # Initialize the result array with zeros, where ans[i] will store
        # the exclusive time for function i
        ans = [0] * n
        
        # Initialize an empty stack to keep track of function call timings.
        # Each element in the stack will be a list [function_id, timestamp],
        # where `timestamp` indicates the time the function started.
        stack = []
        
        # Loop through each log entry in the logs
        for log in logs:
            # Split the log into function ID, event type (start/end), and timestamp
            f_id, event, time = log.split(':')
            f_id, time = int(f_id), int(time)  # Convert function ID and time to integers
            
            if event == 'start':
                # If the event is a "start" and there's already a function on the stack,
                # update the exclusive time of the function on top of the stack.
                # This calculates the time spent on the function until this new start.
                if stack:
                    ans[stack[-1][0]] += time - stack[-1][1]
                
                # Push the new function with its start time onto the stack
                stack.append([f_id, time])
            else:
                # If the event is "end", pop the function from the stack
                popped = stack.pop()
                
                # Calculate the exclusive time for the function at the top of the stack
                # and add it to the result for that function. +1 is added because "end" is inclusive.
                ans[popped[0]] += time - popped[1] + 1
                
                # Update the timestamp of the function now on top of the stack (if there is one)
                # to reflect that it resumes right after the current function ends.
                if stack:
                    stack[-1][1] = time + 1  # Reset start time for the resumed function
                
        # Return the final list of exclusive times for each function
        return ans

# Time Complexity (TC): O(L), where L is the number of logs.
# - We iterate through each log exactly once, performing O(1) operations for each log.

# Space Complexity (SC): O(N + L), where:
# - O(N) is for the `ans` array, which stores exclusive time for each of the `n` functions.
# - O(L) is for the `stack`, which, in the worst case, can hold all logs if all are "start" logs consecutively.
