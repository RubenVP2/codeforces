class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        for idx, char in enumerate(word1):
            try:
                if idx == len(word1) - 1:
                    merged += char + word2[idx:]
                    continue    
                merged += char + word2[idx]
            except IndexError:
                merged += word1[idx:]
                break
        return merged

print(Solution().mergeAlternately('abc', 'pqr')) # apbqcr