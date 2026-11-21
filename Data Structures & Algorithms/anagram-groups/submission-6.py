class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}

        for word in strs:
            sort_word = "".join(sorted(word))
            if sort_word not in dictionary:
                dictionary[sort_word] = [word]

            elif sort_word in dictionary:
                dictionary[sort_word].append(word)
        
        return list(dictionary.values())
        