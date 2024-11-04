class Solution:
    def compressedString(self, word: str) -> str:
        #comp = ""  # NOT HELPFUL IN PYTHON AS STRINGS ARE IMMUTABLE SO INEFFICIENT
        comp = []
        n = len(word)
        i = 0
        while i<n: # O(n)
            char_count = 0
            char = word[i]
            while i<n and char_count < 9 and char == word[i]: # O(1) because each char is visited only once
                char_count += 1
                i += 1  
          
            #comp += str(char_count) + char # O(9) NOT HELPFUL IN PYTHON AS STRINGS ARE IMMUTABLE SO INEFFICIENT
            comp.append(str(char_count))
            comp.append(char)
        return "".join(comp)
# T.C = O(n), where n is lenght of word
# S.C = O(n)