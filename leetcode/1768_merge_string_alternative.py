class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_chars = []
        # Itère sur les deux chaînes simultanément
        for char1, char2 in zip(word1, word2):
            merged_chars.append(char1)
            merged_chars.append(char2)
        # Ajoute les caractères restants de la chaîne la plus longue
        longer_tail = word1[len(merged_chars)//2:] if len(word1) > len(word2) else word2[len(merged_chars)//2:]
        merged_chars.append(longer_tail)
        # Convertit la liste en chaîne
        return ''.join(merged_chars)

print(Solution().mergeAlternately('abc', 'pqr')) # apbqcr