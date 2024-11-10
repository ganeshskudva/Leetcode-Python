def validIPAddress(self, IP):
        # Helper function to validate if a segment is a valid IPv4 component
        def isIPv4(s):
            try:
                # Convert to integer and check if the integer string matches the original
                # string to avoid cases like "01", which is invalid in IPv4
                # Check if it lies within the valid IPv4 range (0 to 255)
                return str(int(s)) == s and 0 <= int(s) <= 255
            except:
                return False

        # Helper function to validate if a segment is a valid IPv6 component
        def isIPv6(s):
            try:
                # Check if the length is 4 or less and if it's a valid hexadecimal number
                return len(s) <= 4 and int(s, 16) >= 0
            except:
                return False

        # Step 1: Check for IPv4
        # IPv4 should have exactly 3 dots and each segment must satisfy IPv4 criteria
        if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
            return "IPv4"

        # Step 2: Check for IPv6
        # IPv6 should have exactly 7 colons and each segment must satisfy IPv6 criteria
        if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
            return "IPv6"

        # If neither IPv4 nor IPv6, return "Neither"
        return "Neither"

# Time Complexity (TC):
# - Checking IP.count(".") and IP.count(":") both take O(N), where N is the length of IP.
# - For IPv4: IP.split(".") takes O(N), and checking each segment with isIPv4 takes O(1),
#   so overall IPv4 check is O(N).
# - For IPv6: IP.split(":") takes O(N), and checking each segment with isIPv6 takes O(1),
#   so overall IPv6 check is also O(N).
# - Overall time complexity is O(N), where N is the length of the IP string.

# Space Complexity (SC):
# - IP.split(".") or IP.split(":") each create a list of segments, costing O(N) space.
# - Helper functions do not use additional space except for temporary variables.
# - Overall space complexity is O(N), due to the space required to store split segments.
