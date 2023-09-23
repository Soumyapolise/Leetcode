class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
    
        # Create a dictionary to store the longest chain length for each word
        dp = {}

        # Initialize the result to 1 (minimum chain length for any word)
        result = 1

        # Iterate through each word in the sorted order
        for word in words:
            # Initialize the longest chain length for this word to 1
            dp[word] = 1

            # Try to remove each character from the word to find predecessors
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)

            # Update the overall result if needed
            result = max(result, dp[word])

        return result